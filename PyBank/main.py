#---------------------------------------------------------------------------------------------------------------------------------------------------------

# This script reads the data contained in the budget_data.csv, once analysed, the following is outputted to the terminal and exported into a text file:

# 1) The total number of months included in the data set.
# 2) The net total amount of "Profit/Losses" over the entire period.
# 3) The changes in "Profit/Losses" over the entire period, and then the average of those changes.
# 4) The greatest increase in profits (date and amount) over the entire period.
# 5) The greatest decrease in profits (date and amount) over the entire period.

# Recommended: familarise yourself with the budget_data.csv before reviewing the below script. 

#---------------------------------------------------------------------------------------------------------------------------------------------------------

#Imports Dependencies
import os                                                                                              # Allows us to create a usable file path accross operating systems. 
import csv                                                                                             # This module allows us to read CSV files.

# os.path navigates to current working directory and joins on the specified path to find to the budget_data.csv file. 
csvpath = os.path.join('Resources', 'budget_data.csv')

# This code block enables reading of the budget_data.csv file:
with open(csvpath) as csvfile:                                                                         # Opens the budget_data.csv and sets 'csvfile' as it's alias.

    csvreader = csv.reader(csvfile, delimiter=',')                                                     # The 'csvreader' variable reads the budget_data.csv's contents in a format where columns are seperated by a comma delimiter.
  
    csv_header = next(csvreader)                                                                       # The budget_data.csv has headers, so it will need to be overlooked for calculus.
   

    # Declares the variables and lists used in the script.
    Date_List = []                                                                                     # Creates a bare list to store the date each profit/ loss in budget_data.csv was recorded against. 

    PL_List = []                                                                                       # Creates a bare list to store the monthly profit and loss figures in. 

    Profit_Change = []                                                                                 # Creates a bare list to store the monthly profit changes within.

    Previous_Profit = 0                                                                                # 'Previous_Profit is defined as a variable, it will be used to help calculate changes between monthly profits. 

    # For loop - Reads through each row in the budget_data.csv which has been read and printed earlier in the script.
    for row in csvreader:

        Date_List.append(row[0])                                                                       # Adds each observed date into the 'Date_List'.

        PL_List.append(int(row[1]))                                                                    # Adds each observed profit/loss figure into the 'PL_List'.

        Difference = int(row[1]) - Previous_Profit                                                     # Stores the difference between the observed profit/loss figure and the previous profit figure in a variable named 'Difference'.
        
        Profit_Change.append(Difference)                                                               # Adds each change in profit observation to the 'Profit_Change' list. 

        Previous_Profit = int(row[1])                                                                  # Sets the value of 'Previous_Profit' to be the current observed profit/loss figure; by the next loop it will be the previous profit. 

    
    # Sets the 'Average_Change' variable to equal the sum of the profit changes (from the 1st index onwards) and divides it by the number of monthly changes.
    Average_Change = round(sum(Profit_Change[1:])/ (len(Profit_Change) - 1),2)

    # Compiles the lists of profit/ loss: dates, figures, and monthly differences into one zipped tuple. 
    Budget_Data = zip(Date_List, PL_List, Profit_Change)

    # For loop - Reads through each row in the 'Budget_Data' zipped tuple.
    for row in Budget_Data:

        if row[2] == int(max(Profit_Change)):                                                          # Conditional: if the observed profit/ loss difference equals the maximum profit increase...
            max_month = row[0]                                                                         # When condition met: set the max_month variable to equal the corresponding date. 

        if row[2] == int(min(Profit_Change)):                                                          # Conditional: if the observed profit change value equals the maximum profit decrease...
            min_month = row[0]                                                                         # When condition met: Set the min_month variable to equal the corresponding date. 
    
    # Prints analysis out to user in the terminal:
    print("\n")                                                                                        # Formatting: creates a new line before output heading for easier reading.

    print("Financial Analysis")                                                                        # Financial Analysis heading for output.

    print("\n----------------------------\n")                                                          # Formatting: divider for output. 

    print(f"Total Months: {len(Date_List)}\n")                                                         # Total number of months in the budget_data.csv that were stored in the 'Date_List'.

    print(f"Total: ${sum(PL_List)}\n")                                                                 # Net sum of the profit/ losses figures in the budget_data.csv that were stored in the 'PL_List'.

    print(f"Average Change: ${Average_Change}\n")                                                      # Average of the profit/ loss differences over the entire period; obtained from the 'Average_Change' variable.

    print(f"Greatest Increase in Profit: {max_month} (${max(Profit_Change[1:])})\n")                   # The greatest increase in profits (date and amount) over the entire period.

    print(f"Greatest Decrease in Profit: {min_month} (${min(Profit_Change[1:])})\n")                   # The greatest decrease in profits (date and amount) over the entire period.


# os.path navigates to current working directory and joins on the specified path to find to the analysis.txt file. 
output_path = os.path.join('analysis', 'analysis.txt')

# Opens the analysis.txt file in a "write" mode and and sets 'output_file' as it's alias.
with open(output_path, 'w') as output_file:

    # Exports the financial analysis into the analysis.txt document; creating a new line after each write output. 
    output_file.write(f"Financial Analysis")                                                           # Financial Analysis heading for export.

    output_file.write(f"\n\n----------------------------\n\n")                                         # Formatting: divider for export. 

    output_file.write(f"Total Months: {len(Date_List)}\n\n")                                           # Exports the total number of months in the budget_data.csv that were stored in the 'Date_List'.

    output_file.write(f"Total: ${sum(PL_List)}\n\n")                                                   # Exports the net sum of the profit/ losses figures in the budget_data.csv that were stored in the 'PL_List'.

    output_file.write(f"Average Change: ${Average_Change}\n\n")                                        # Exports the average of the profit/ loss differences over the entire period; obtained from the 'Average_Change' variable.

    output_file.write(f"Greatest Increase in Profit: {max_month} (${max(Profit_Change[1:])})\n\n")     # Exports the greatest increase in profits (date and amount) over the entire period.

    output_file.write(f"Greatest Decrease in Profit: {min_month} (${min(Profit_Change[1:])})\n\n")     # Exports the greatest decrease in profits (date and amount) over the entire period.

    output_file.close()                                                                                # Closes the analysis.txt file. 



