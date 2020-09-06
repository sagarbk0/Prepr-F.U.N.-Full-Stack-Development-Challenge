# Prepr F.U.N. Full-Stack Developer Challenge

## Overview
In this challenge, I created a Python program which reads questions from a web article, outputs them into a CSV file and sends a random question as an email.

## Process
1.	I used the Requests module to get the webpage, and LXML’s HTML module to get its content and parse it (selecting h2 header text)
2.	The h2 elements, which contained the questions, were stored in a list
3.	I iterated through the list with the questions to clean them, i.e. remove the indices and unneeded sections.
4.	I saved the list in a Pandas dataframe, and converted the data frame  to a CSV file. (Alternatively, I could’ve used the CSV module to complete the task: the code for that approach also is provided)
5.	I selected a random question from the list using the random module.
6.	I created the webhook on IFTTT.com and with the link with my key, I posted a request using the requests module, with the random question in the data.
7.	I verified that I was able to get the emails.
![Question Image](https://i.ibb.co/FxyCSXy/Random-Question.png)
 
## Next Steps
To create a GUI or web application which enables users to process similar webpages and send the results to their emails.