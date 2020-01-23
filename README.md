# enron_emails
A program that parses Enron Emails dataset. Dataset version that was used is May 7, 2015. The dataset is public and can be found from https://www.cs.cmu.edu/~./enron/.

The program first parses all emails in Enron Email -dataset and counts into a first csv (emails_sent_totals.csv) the total amounts of each emails sender and each emails receiver and calculates the totals from all emails: how many emails were sent from each sender address to each recipient. (not usernames, but all sender addresses to all receiving addresses.)

In the second csv (emails_sent_average_per_weekday.csv) only users inbox folders are parsed, and it counts the average amount of received emails per user per day.

The program calculates:
  1) how many emails were sent from each sender address to each recipient in all emails, and
  2) the average number of emails received into inbox folder per day per employee per day of week (monday, tuesday, etc.).


## Instructions to run the programmes.

This repository contains the program enron_emails_program.py. The ipython versions are working progress and contains tasks separately.

The program uses mostly Python's built in libraries that are first imported. Only one library, pandas-library need to be installed.

The program might take some time to finish as in first task it uses the whole email dataset, all mails for all users which is quite large, but on the second part it only considers all inboxes of users.

### To run program, run enron_emails_program.py

To run the code, run enron_emails_program.py. 

To execute code, give the path to enron emails maildir to class in main function: Enron_emails('add/path/here/enron_emails/maildir'), 
Path should point to the file location where the actual location of Enron Emails -dataset is located. Here the location has been: C:\path\to\enron_emails\maildir.

In main function you also need to give to method the location of where you want to save the first csv-file:
count_similarities('csv/path/here'),
to create the emails_sent_totals.csv. Also, to calculate the average of mails per user, give in main also the folder path to where you want to save the second csv file (called emails_sent_average_per_weekday.csv): 
calculate_emails_average_per_day('path\to\csv\folder).

Use ''- marks to give the path to the program. Also, if using windows paths, use key r infront of '', i.e. r'path/to/email/set' - as windows path is not recognized otherwise and errors accure. If using Linux or Mac no need to use keyword r. 

The program outputs two None's and finally 'Finished' when it has run the program and created the two csv-files into given location.
