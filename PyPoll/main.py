#---------------------------------------------------------------------------------------------------------------------------------------------------------

# This script reads the data contained in the election_data.csv, once analysed, the following is outputted to the terminal and exported into a text file:

# 1) The total number of votes cast. 
# 2) A complete list of candidates who recieved votes.
# 3) The percentage of votes each candidate won. 
# 4) The total number of votes each candidate won. 
# 5) The winnder of the election based on popular vote. 

# Recommended: familarise yourself with the election_data.csv before reviewing the below script. 

#---------------------------------------------------------------------------------------------------------------------------------------------------------

#Imports Dependencies 
import os                                                               # Allows us to create a usable file path accross operating systems. 
import csv                                                              # This module allows us to read CSV files.

# os.path navigates to current working directory and joins on the specified path to find to the election_data.csv file. 
csvpath = os.path.join('Resources', 'election_data.csv')

# This code block enables reading of the election_data.csv file:
with open(csvpath) as csvfile:                                          # Opens the election_data.csv and sets 'csvfile' as it's alias.

    csvreader = csv.reader(csvfile, delimiter=',')                      # The 'csvreader' variable reads the election_data.csv's contents in a format where columns are seperated by a comma delimiter.
    
    csv_header = next(csvreader)                                        # The election_data.csv has headers, so it will need to be overlooked for calculus.


    # Creation of lists and dictionary used in the script.
    Candidate_List = []                                                 # Creates a bare list to store the election's participating candidates within.

    Total_Votes = []                                                    # Creates a bare list to store each of the participating candidates' total votes within.

    Vote_Results = {}                                                   # Creates a bare dictionary to store the key-value pairs for candidates' and their vote counts.
    

    Candidate_Analysis = []                                             # Creates a bare list to store the candidates final popularity statistics within. [Helper for exporting text file]. 


    # For loop - Reads through each row in the election_data.csv which has been read and printed earlier in the script.
    for row in csvreader:
        
        Candidate_Key = row[2]                                          # Sets up a 'Candidate_Key' variable to equal the observed candidate's name.

        if Candidate_Key not in Vote_Results:                           # Conditional: if the candidates name is not already in 'Vote_Results' dictionary...

            Vote_Results[Candidate_Key] = []                            # When condition met: A new key in the Vote_Results dictionary is created for the candidate with their name.

        Vote_Results[Candidate_Key].append(1)                           # Tallies one value onto the observed candidates' key in the Vote_Results dictionary.

    
    # For loop - Reads through each value in the Vote_Results dictionary (where each value represents a tally for a vote made).
    for value in Vote_Results.values():

        Vote_Count = sum(value)                                         # Sets up a 'Vote_Count' variable which equals the sum of each candidate's tally values stored in the 'Vote_Results' dictionary.                                                                                      
        
        Total_Votes.append(Vote_Count)                                  # Adds the 'Vote_Count' into the 'Total_Votes' list.    

    
    # For loop - Reads through each key in the Vote_Results dictionary.
    for Candidate_Key in Vote_Results:                          
        
        Candidate_List.append(Candidate_Key)                            # Adds candidate's name into the 'Candidate_List'. 

    
    # Zips the candidate's names and each of their total votes lists into one tuple called 'Election_Results' (ready to be used as a iterator). 
    Election_Results = zip(Candidate_List, Total_Votes)

    # Prints the election results out in the terminal.
    print("\n")                                                         # Formatting: creates a new line before output heading for easier reading.

    print("Election Results")                                           # Election Results heading for output.
                                
    print("\n-------------------------\n")                              # Formatting: divider for output.
    
    print(f"Total Votes: {sum(Total_Votes)}")                           # Outputs the total votes accross all candidates.
    
    print("\n-------------------------")                                # Formatting: divider for output.

    
    # For loop - Reads through each row in the 'Election_Results' zipped list.
    for row in Election_Results:

        if row[1] == max(Total_Votes):                                  # Conditional: If the candidate's total votes is equal to the highest value in the Total_Votes list...
            
            winner = row[0]                                             # Sets the 'winner' variable to equal the candidate's name.            
        
        percentage = round((row[1]/sum(Total_Votes))*100, 3)            # Calculates the percentage of votes each candidate secured and rounds to 3 d.p.
        
        print(f"\n{row[0]}: {percentage}% ({row[1]})")                  # Outputs the candidate name, their percentage of the total vote, and the total votes they secured.
        
        # Adds each of candidates statistics to the 'Candidate_Analysis' list to help with the txt export. 
        Candidate_Analysis.append(f"{row[0]}: {percentage}% ({row[1]})")
    
    
    print("\n-------------------------\n")                              # Formatting: divider for output.
    
    print(f"Winner: {winner}")                                          # Outputs winner's name. 
    
    print("\n-------------------------")                                # Formatting: divider for output.

    
# Navigates to the analysis text file where the output of the analysis will be stored. 
output_path = os.path.join('analysis', 'analysis.txt')

# Opens the analysis.txt file in a "write" mode and sets 'output_file' as it's alias.
with open(output_path, 'w') as output_file:

    # Exports the election analysis into the analysis.txt document. 
    output_file.write(f"Election Results")                              # Election Results heading for export.

    output_file.write(f"\n\n----------------------------\n\n")          # Formatting: divider for export. 

    output_file.write(f"Total Votes: {sum(Total_Votes)} \n\n")          # Exports the total votes accross all candidates.

    output_file.write(f"---------------------------- \n\n")             # Formatting: divider for export. 
    seperator = "\n\n"                                                  # Formatting: two new lines. 

    output_file.write(f"{seperator.join(Candidate_Analysis)} \n\n")     # Exports the candidate name, their percentage of the total vote, and the total votes they secured.

    output_file.write(f"---------------------------- \n\n")             # Formatting: divider for export. 

    output_file.write(f"Winner: {winner} \n\n")                         # Exports the winner's name.

    output_file.write(f"----------------------------")                  # Formatting: divider for export.        

    output_file.close()                                                 # Closes the analysis.txt file. 
       




