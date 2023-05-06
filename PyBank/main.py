#Imports Modules
import os                                                       # Allows us to create a usable file path accross operating systems. 
import csv                                                      # This module allows us to read CSV files.

# Navigates to current working directory and then to the budget_data.csv
csvpath = os.path.join('..', 'Resources', 'budget_data.csv')

#Reading the budget_data.csv file:
with open(csvpath) as csvfile:                                  # Opens the budget_data.csv and stores the contents in the variable 'csvfile'.

    csvreader = csv.reader(csvfile, delimiter=',')              # The 'csvreader' variable stores the CSV's contents in a format where columns are seperated by a comma delimiter.

    print(csvreader)                                            # Prints the contents of the csvreader. 

    
    csv_header = next(csvreader)                                # The budget_data.csv has headers, so it will need to be overlooked for calculus.
    
    # Declares the variables and lists used in the script.
    Date_List = []                                              # Creates a bare list to store the budget dates in.
    PL_List = []                                                # Creates a bare list to store the profit and loss figures in. 
    Profit_Change = []                                          # Creates a bare list to store the monthly profit changes within.
    Previous_Profit = 0                                         # Will be used to help calculate changes between monthly profits. 

    # For loop begun to read through each row in the budget_data.csv. 
    for row in csvreader:                                       
        Date_List.append(row[0])                                # Adds each date in the budget_data.csv to the Date_List. 
        PL_List.append(int(row[1]))                             # Adds each profit/loss figure from the budget_data.csv to the PL_List.

        Change = int(row[1]) - Previous_Profit                  # Stores the difference between the value in column one of the CSV and Previous_Profit in a variable named 'Change'.
        Profit_Change.append(Change)                            # Adds each change in profit observation to the Profit_Change list. 

        Previous_Profit = int(row[1])                           # Sets the value of Previous_Profit to be the current observed row; by the next loop it will be the previous profit. 

    Budget_Data = zip(Date_List, PL_List, Profit_Change)        # Compiles each of the three lists in this script into one zipped list. 

    
    
    # For loop begun to read through each row in the Budget_Data zipped list.
    for row in Budget_Data:
        if row[2] == int(max(Profit_Change)):                   # Conditional: if the observed profit change value equals the maximum profit increase...
            max_month = row[0]                                  # Set the max_month variable to equal the corresponding date. 

        if row[2] == int(min(Profit_Change)):                   # Conditional: if the observed profit change value equals the maximum profit decrease...
            min_month = row[0]                                  # Set the min_month variable to equal the corresponding date. 

    # Sets the average variable to equal the sum of the profit changes (from the 2nd row onwards) and divides it by the number of monthly changes.
    Average = round(sum(Profit_Change[1:])/ (len(Profit_Change) - 1),2)
    
    # Prints analysis out to user:
    print("")                                                                      # Creates space before input for easier reading.
    print("Financial Analysis")                                                    # Financial Analysis heading for output.
    print("----------------------------")                                          # Output formatting. 
    print(f"Total Months: {len(Date_List)}")                                       # Total number of months in the budget_data.csv.
    print(f"Total: ${sum(PL_List)}")                                               # Net sum of the profit/ losses in the budget_data.csv.
    print(f"Average Change: ${Average}")                                           # Average of the changes in profit/ loss over the entire period.
    print(f"Greatest Increase in Profit: {max_month} (${max(Profit_Change)})")     # The greatest increase in profits (date and amount) over the entire period.
    print(f"Greatest Decrease in Profit: {min_month} (${min(Profit_Change)})")     # The greatest decrease in profits (date and amount) over the entire period.

# Navigates to the analysis text file where the output of the analysis will be stored.
output_path = os.path.join('..', 'analysis', 'analysis.txt')

# Opens the analysis.txt file in a "write" mode and holds this in the variable 'output_file'.
with open(output_path, 'w') as output_file:

    # Outputs the financial analysis into the analysis.txt document, creating a new line after each write output. 
    output_file.write(f"Financial Analysis \n")
    output_file.write(f"---------------------------- \n")
    output_file.write(f"Total Months: {len(Date_List)} \n")
    output_file.write(f"Total: ${sum(PL_List)} \n")
    output_file.write(f"Average Change: ${Average} \n")
    output_file.write(f"Greatest Increase in Profit: {max_month} (${max(Profit_Change)}) \n")
    output_file.write(f"Greatest Decrease in Profit: {min_month} (${min(Profit_Change)}) \n")

    output_file.close()                                                            # Closes the analysis.txt file. 



