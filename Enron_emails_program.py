#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 23 01:27:34 2020

@author: Anette Karhu
"""

from email.parser import BytesHeaderParser
import pandas as pd
import os
import csv
from pathlib import Path
import time
import itertools
from email.utils import parsedate_to_datetime
import re

class Enron_emails:
    '''
    A class to handle enron emails.
    Goes through all enron emails from the dataset.
    
    First, it counts how many times a each sender has sent to a
    each receiver emails and saves this information into a csv called:
    'emails_sent_totals.csv'.
    
    Second, it calculates the average of all emails a user has gotten 
    per week day and saves it into a csv called:
    'emails_sent_average_per_weekday.csv'.
    '''
    FOLDER = 'inbox'
    def __init__(self, root_directory, csv_save_path):
        '''
        Initialize with root directory of where the enron emails are located,
        and with path where to save the csv-files.
        '''
        self.root_directory = root_directory
        self.csv_save_path = csv_save_path
    
    def users_directories_files(self):
        '''
        List of paths to all files for all users.
        Used for reading email data from all users and all folders.
        '''
        all_dirs = [(os.path.join(root,file)) for root,dirs,files in os.walk(self.root_directory) for file in files]
        return all_dirs

    def users_inbox_files(self):
        '''
        List of all users from selected folder (self.FOLDER sets the wanted folder) 
        paths to count receivers.
        Used for reading email data from all users and from selected folder.
        '''
        selected_folder = [ os.path.join(root,_dir) for root, dirs, files in os.walk(r'C:\Users\Anette\Documents\Enron_Emails_project\enron_emails\maildir') for _dir in dirs if _dir == self.FOLDER]
        folder_paths = [os.path.join(root,file) for path in selected_folder for root,dirs,files in os.walk(path) for file in files]
        return folder_paths

    def load_parse_and_save(self, file_path):
        '''
        Loads all email data and opens them in binary. Function parses From, To, Cc, and Bcc headers
        with BytesHeaderParser and saves parsed email addresses first into list of tuples and then 
        into a csv-file if they contain values. This new csv-file has two columns, the receiver 
        and the sender email addresses. 
        '''
        sender_receiver_list =[]
        for index, mail in enumerate(self.users_directories_files()):
            with open(mail, 'rb') as fp:             
                email = BytesHeaderParser().parse(fp)
                # parse with email headers to get only sender and receivers.
                sender = format(email['from'])
                # Makes a list of tuples, without 'None' strings.
                if format(email['to']) != 'None':
                    receiver = format(email['to'])
                    sender_receiver_list.append((sender, receiver))
                if format(email['cc']) != 'None':
                    cc_receiver = format(email['cc'])
                    sender_receiver_list.append((sender, cc_receiver))
                if format(email['bcc']) != 'None':
                    bcc_receiver = format(email['bcc'])
                    sender_receiver_list.append((sender, bcc_receiver))
        # write tuple into csv at once to save space.
        csv_writer = csv.writer(open(file_path, 'w', newline='', encoding="utf-8"))
        csv_writer.writerows(sender_receiver_list)
        return

    def count_similarities(self):
        '''
        This function calls load_parse_and_save() function to parse data.
        Then it opens the created csv-file with pandas DataFrame and
        cleans special characters from email data. Next, it splits tuples from 
        the receiver-column into their own rows, having now only one sender and 
        one receiver in a row. Finally, the function counts the same senders 
        and receivers totals from all emails and saves this information into 
        csv-file's new count-column.
        '''
        csv_file_path = os.path.join(self.csv_save_path , 'emails_sent_totals.csv')
        # load csv data as dataframe, make columns.
        self.load_parse_and_save(csv_file_path)
        csv_as_df = pd.read_csv(csv_file_path)
        csv_as_df.columns=['sender','receiver']
        # remone (), specials characters from email addresses.
        csv_as_df['receiver'] = csv_as_df['receiver'].str.replace("\(\'", '')
        csv_as_df['receiver'] = csv_as_df['receiver'].str.replace("\',\)", '')
        # remove any word before <. appears in string, and remove <.> - characters.
        csv_as_df['receiver'] = [re.sub(r".*<.", '', stri) for stri in csv_as_df['receiver']]
        csv_as_df['receiver'] = csv_as_df['receiver'].str.replace(">", '')
        # Splits the receivers into own rows.
        splitted_receivers_df = pd.concat([pd.Series(row['sender'], row['receiver'].split(', ')) for _, row in csv_as_df.iterrows()]).reset_index()
        splitted_receivers_df.columns =['receiver', 'sender']
        splitted_receivers_df = splitted_receivers_df.reindex(columns=['sender', 'receiver'])
        # Counts the same receivers and senders amount together. (flips the columns and forgets colum names.)
        counted_data = splitted_receivers_df.pivot_table(index=['sender', 'receiver'], aggfunc='size')
        # switch columns back into order and rename columns into asked format:sender,receiver,count.
        counted_data = pd.DataFrame(counted_data)
        counted_data.rename(columns={0:'count'}, inplace=True)
        counted_data.to_csv(csv_file_path)
        return
        
    def dates_parsing(self):
        '''
        Parses a week day from all emails headers and gets the date of emails
        for comparison purposes. Changes weekdays to numbers, from 0-6, 
        0=Monday, 6=Sunday etc. Saves this information to csv for memory reasons.
        '''
        user_date_list =[]  
        for index, mail in enumerate(self.users_inbox_files()):
            with open(mail, 'rb') as fp:   
                # Parse only header information from emails.
                email = BytesHeaderParser().parse(fp)
                # Select date from headers of emails and split only needed information: date and day for comparison.
                parse_dates = format(email['Date'])
                date= parsedate_to_datetime(parse_dates).date()
                weekdays = parse_dates.split(',' )[0]
                # Change weekdays to num [0,6]
                days_as_num = time.strptime(weekdays, '%a').tm_wday
                folder_names = Path(mail).parts
                usernames = os.listdir(self.root_directory)
                # make a list of emails username, day of week and date for comparison.
                user_day_list = [(username,days_as_num, date) for folder_name in folder_names for username in usernames if username in folder_name]
                user_date_list.append(list(itertools.chain(*user_day_list)))
        csv_file_path = os.path.join(self.csv_save_path , 'emails_sent_average_per_weekday.csv')
        csv_writer = csv.writer(open(csv_file_path, 'w', newline=''))
        csv_writer.writerows(user_date_list)
        return csv_file_path
    
    def calculate_emails_average_per_day(self):
        '''
        Calculate the average amount of emails per day per user.
        First it calls the dates_parsing() to parse all email data and create
        csv draft with parsed data.
        Next, reads csv file and adds column names. Counts duplicate rows together
        and then calculates the average for each sender and each week day emails.
        
        '''
        csv_path = self.dates_parsing()
        csv_to_df = pd.read_csv(csv_path)
        csv_to_df.columns = ['employee', 'day_of_week', 'date']
        duplicates_in_data_df = csv_to_df.pivot_table(index=['employee', 'day_of_week', 'date'], aggfunc='size')
        duplicates_in_data_df = pd.DataFrame(duplicates_in_data_df)
        duplicates_in_data_df.rename(columns={0:'counter'}, inplace=True)
        average_mails = duplicates_in_data_df.groupby(['employee', 'day_of_week']).mean()
        average_mails.to_csv(csv_path)
        return
    
    
def main():
    '''
    The main function to call the program. The program goes through all emails
    in Enron Email -dataset and first counts into a csv (emails_sent_totals.csv) 
    the total amounts of each sender sent mail to each receiver, and then
    counts from all received (inboxes) emails of all users average per day.
    
    When program has executed, it prints Finished. Csv-files have been created into given paths.
    '''
    enron_all_mails = Enron_emails(r'C:\Users\Anette\Documents\Enron_Emails_project\enron_emails\maildir', r'C:\Users\Anette\Documents\enron_emails')
    Enron_emails.count_similarities(enron_all_mails)
    Enron_emails.calculate_emails_average_per_day(enron_all_mails)
    print('Finished')
    
if __name__ == "__main__":
    main()
