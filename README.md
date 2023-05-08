# python-challenge
This repository contains two Python challenges named: PyBank, and PyPoll. Both scripts will analyse data from their respective csv files: budget_data.csv and election_data.csv to output and export summaries of the findings for the user. 

**PyBank:**
Analyses the financial records of a fictional company which are stored in a file named budget_data.csv. The budget_data.csv file contains information about monthly profit and loss figures which are logged against their respective dates; The dataset is composed of two columns: "Date" and "Profit/Losses". 

The output/ export will contain the results of the calculations for:
- The total number of months included in the dataset
- The net total amount of "Profit/Losses" over the entire period
- The changes in "Profit/Losses" over the entire period, and then the average of those changes
- The greatest increase in profits (date and amount) over the entire period
- The greatest decrease in profits (date and amount) over the entire period

![image](https://user-images.githubusercontent.com/126973634/236814219-85d3718d-058d-4e6e-9b13-32d92b1bf9c5.png)

Folder Breakdown for PyBank:
PyBank > main.py - the python script used to analyse the budget_data.csv.
PyBank > Resources - this folder contains the budget_data.csv file read by the main.py script.
PyBank > analysis - this folder contains the analysis.txt file where the results are exported to each time the main.py code is run. 

**PyPoll:**
Analyses the election results of a fictional small rural town which are stored in a file named election_data.csv. The election_data.csv file contains information about the votes recieved by candidates; The dataset is composed of three columns: "Ballot ID" and "County", and "Candidate". 

The output/ export will help the town to modernise its vote counting process by showing the results of the calculations for:
- The total number of votes cast
- A complete list of candidates who received votes
- The percentage of votes each candidate won
- The total number of votes each candidate won
- The winner of the election based on popular vote

![image](https://user-images.githubusercontent.com/126973634/236815941-ff8f300e-2916-4952-8038-4f13d6a09101.png)

Folder Breakdown for PyPoll:
PyPoll > main.py - the python script used to analyse the election_data.csv.
PyPoll > Resources - this folder contains the election_data.csv file read by the main.py script.
PyPoll > analysis - this folder contains the analysis.txt file where the results are exported to each time the main.py code is run. 

