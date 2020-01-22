# enron_emails
A program that parses Enron Emails dataset. 

The program calculates:
  1) how many emails were sent from each sender address to each recipient, and
  2) the average number of emails received per day per employee per day of week (monday, tuesday, etc.).

Dataset version that was used is May 7, 2015. The dataset is public and can be found from https://www.cs.cmu.edu/~./enron/.

## Instructions to run the programmes.

This repository contains two python programs. One for task 1, Enron_emails.ipynb, and for task two: enron_emails_task_2.ipynb.

Both programmes uses mostly Python's built in libraries that are first imported. Only one library, pandas-library need to be installed.

The programs might take some time (10-50min depending on computer) to finish as they both use the whole email dataset, all mails for all users.

### To run task 1: run Enron_emails.ipynb:

To run the code, run all cells in ipython. The program goes through all emails in Enron Email -dataset and counts into a csv (emails_sent_totals.csv) the total amounts of each sender sent mail to each receiver.

To execute code, give the path to enron emails maildir to class in main function: Enron_emails('add/path/here/enron_emails/maildir'), 
Path should point to the file location where the actual location of Enron Emails -dataset is located. Here the location has been: C:\path\to\enron_emails\maildir.

In main function you also need to give to method the location of where you want to save the csv-file:
count_similarities('csv/path/here'), to create the emails_sent_totals.csv.

Use ''- marks to give the path to the program. Also, if using windows, use key 'r', i.e. r'path/to/email/set' - as windows path is not recognized otherwise and errors accure. If using Linux or Mac 'path/to/email/set'- is enough, don't use r'path/to/email/set'.

When program has executed, None appears. A csv-file has been created into given path.

### To run task 2: run enron_emails_task_2.ipynb:

To run the code, run all cells in ipython. In main you need to give the path where your enron emails maildir (C:\path\to\enron_emails\maildir) is located for the class in following way: Enron_emails_average('path\to\all\enron\mails\root\maildir').

To calculate the average of mails per user, give in main also the folder path to where you want to save the csv file (called emails_sent_average_per_weekday.csv): Enron_emails_average.calculate_emails_average_per_day('path\to\csv\folder)

The program outputs None when it has run the program and created the csv file to given location.
