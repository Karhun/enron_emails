# enron_emails
A program that parses Enron Emails dataset. Dataset version that was used is May 7, 2015. The dataset is public and can be found from https://www.cs.cmu.edu/~./enron/.

The program first parses all emails in Enron Email -dataset and counts into a first csv (emails_sent_totals.csv) the total amounts of each emails sender and each emails receiver and calculates the totals from all emails: how many emails were sent from each sender address to each recipient. (not usernames, but all sender addresses to all receiving addresses.)

In the second csv (emails_sent_average_per_weekday.csv) only users inbox folders are parsed, and it counts the average amount of received emails per user per day. (All users did not have inbox folder, so they do not appear in this task).

The program calculates:
  1) how many emails were sent from each sender address to each recipient in all emails, and
  2) the average number of emails received into inbox folder per day per employee per day of week (monday, tuesday, etc.).


## Instructions to run the programmes.

This repository contains the program enron_emails_program.py. The ipython versions are working progress and contains the tasks separately.

The program uses mostly Python's built in libraries that are first imported. Only one library, pandas-library need to be installed.

The program might take some time to finish as in the first task it uses the whole email dataset, all mails for all users which is quite large, but on the second part it only considers all inboxes of users, (does not have all users, as some of the users don't have inbox).

### To run program, run enron_emails_program.py

To run the code, run enron_emails_program.py. 

To execute code, give the 2 paths in main function: Enron_emails('add/path/here/enron_emails/maildir', 'csv/path/here').
The paths to be given are:
1) path to enron emails maildir location. ('C:\path\to\enron_emails\maildir')
2) path where to save the two csv-files called emails_sent_totals.csv, and emails_sent_average_per_weekday.csv.
('C:\path\to\csv_save')

Use ''- marks to give the path to the program. Also, if using windows paths, use key r infront of '', i.e. r'path/to/email/set' - as windows path is not recognized otherwise and errors accure. If using Linux or Mac no need to use the keyword r. 

The program outputs 'Finished' when it has run the program and created the two csv-files into given location.
