#Imports Modules
import os                                                       # Allows us to create a usable file path accross operating systems. 
import csv                                                      # This module allows us to read CSV files.

# Navigates to current working directory and then to the election_data.csv
csvpath = os.path.join('Resources', 'election_data.csv')

#Reading the election_data.csv file:
with open(csvpath) as csvfile:                                  # Opens the election_data.csv and stores the contents in the variable 'csvfile'.

    csvreader = csv.reader(csvfile, delimiter=',')              # The 'csvreader' variable stores the CSV's contents in a format where columns are seperated by a comma delimiter.

    print(csvreader)                                            # Prints the contents of the csvreader. 

    
    csv_header = next(csvreader)                                # The election_data.csv has headers, so it will need to be overlooked for calculus.


    # Creation of lists and dictionary used in the script.
    Candidate_List = []                                         # Creates a bare list to store the participating candidates within.
    Total_Votes = []                                            # Creates a bare list to store the participating candidates' total votes within.
    Vote_Results = {}                                           # Creates a bare dictionary to store the key-value pairs for candidates' and their vote counts.
    Candidate_Analysis = []

    # For loop begun to read through each row in the election_data.csv.
    for row in csvreader:
        Candidate_Key = row[2]                                  # Sets Candidate_Key variable to equal the observed candidate name.
        if Candidate_Key not in Vote_Results:                   # Conditional: if candidate name not already in Vote_Results dictionary...
            Vote_Results[Candidate_Key] = []                    # When condition met - creates a new key in the Vote_Results dictionary.
        Vote_Results[Candidate_Key].append(1)                   # Tallies one value onto the candidates' key in the Vote_Results dictionary.

    
    # For loop begun to read through each value in the Vote_Results dictionary.
    for value in Vote_Results.values():
        Vote_Count = sum(value)                                 # Sets Vote_Count variable to equal the sum of all the tally values stored in the Vote_Results dictionary.                                                                                      
        Total_Votes.append(Vote_Count)                          # Adds the Vote_Count sum per candidate into the Total_Votes list.    

    # For loop begun to read through each key in the Vote_Results dictionary.
    for Candidate_Key in Vote_Results:                          
        Candidate_List.append(Candidate_Key)                    # Adds candidate name into the Candidate_List. 

    
    # Zips the Candidate_List and Total_Votes list into one tuple. 
    Election_Results = zip(Candidate_List, Total_Votes)

    # Prints election results out to the user.
    print("")                                                   # Creates space before input for easier reading.
    print("Election Results")                                   # Election Results heading for output.
    print("")                                                   # Creates space before input for easier reading.                                    
    print("-------------------------")                          # Output formatting. 


    print("")                                                   # Creates space before input for easier reading.
    print(f"Total Votes: {sum(Total_Votes)}")                   # Outputs the total votes accross all candidates.
    print("")                                                   # Creates space before input for easier reading.
    print("-------------------------")                          # Output formatting. 
    print("")                                                   # Creates space before input for easier reading.
    
    # For loop begun to read each row in the Election_Results zipped list.
    for row in Election_Results:
        if row[1] == max(Total_Votes):                          # Conditional: If the candidates total votes is equal to the highest value in the Total_Votes list...
            winner = row[0]                                     # Sets winner variable to equal the candidate's name.            
        percentage = round((row[1]/sum(Total_Votes))*100, 3)    # Calculates the percentage of votes each candidate won.
        print(f"{row[0]}: {percentage}% ({row[1]})")            # Outputs the candidate name, percentage of vote associated with them, and the total votes they were awarded.
        print("")                                               # Creates space before input for easier reading.
        Candidate_Analysis.append(f"{row[0]}: {percentage}% ({row[1]})")
    
    print("-------------------------")                          # Output formatting. 
    print("")                                                   # Creates space before input for easier reading.
    print(f"Winner: {winner}")                                  # Outputs winner's name. 
    print("")                                                   # Creates space before input for easier reading.

    print("-------------------------")                          # Output formatting. 

    
# Navigates to the analysis text file where the output of the analysis will be stored.
output_path = os.path.join('..', 'analysis', 'analysis.txt')
output_path = os.path.join('analysis', 'analysis.txt')

# Opens the analysis.txt file in a "write" mode and holds this in the variable 'output_file'.
with open(output_path, 'w') as output_file:

    # Outputs the financial analysis into the analysis.txt document, creating a new line after each write output. 
    output_file.write(f"Election Results \n \n")
    output_file.write(f"---------------------------- \n \n")
    output_file.write(f"Total Votes: {sum(Total_Votes)} \n \n")
    output_file.write(f"---------------------------- \n \n")
    seperator = "\n \n"
    output_file.write(f"{seperator.join(Candidate_Analysis)} \n \n")
    output_file.write(f"---------------------------- \n \n")
    output_file.write(f"Winner: {winner} \n \n")
    output_file.write(f"----------------------------")           




    output_file.close()                                                            # Closes the analysis.txt file. 
       




