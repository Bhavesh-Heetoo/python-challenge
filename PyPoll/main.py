# -*- coding: UTF-8 -*-
"""PyPoll Homework Starter File."""

# Import necessary modules
import csv
import os

# Files to load and output (update with correct file paths)
file_to_load = os.path.join("Resources", "election_data.csv")  # Input file path
file_to_output = os.path.join("analysis", "election_analysis.txt")  # Output file path

# Initialize variables to track the election data

total_votes = 0  # Track the total number of votes cast

# Define lists and dictionaries to track candidate names and vote counts

# To store names of candiates in a list
Candidates = []

# To hold names and vote count
Candiate_votes_count = {}

# Winning Candidate and Winning Count Tracker
#To store the name of the winning candiate
Winning_Candiiate = None
#To Store the max number of votes received
Winning_Votes = 0

# Open the CSV file and process it
with open(file_to_load) as election_data:
    reader = csv.reader(election_data)

    # Skip the header row
    header = next(reader)

    # Loop through each row of the dataset and process it
    for row in reader:
       
        # Print a loading indicator (for large datasets)
        print(". ", end="")

        # Increment the total vote count for each row
        total_votes +=1
        # Get the candidate's name from the row
        candiate = row[2].strip()
        

        # If the candidate is not already in the candidate list, add them
        if candiate not in Candidates:
            #Add to the list
            Candidates.append(candiate)
         
        # Add a vote to the candidate's count
        if candiate in Candiate_votes_count:
            #Increasing Vote count if Candidate is already in list 
            Candiate_votes_count[candiate] += 1
        else:
            # Setting the vote count if not in list
            Candiate_votes_count[candiate] = 1

# Open a text file to save the output
with open(file_to_output, "w") as txt_file:

    # Print the total vote count (to terminal)
    print("Election Results")
    print("------------------------")
    print(f"Total Votes: {total_votes}")
    print("------------------------")

    # Write the total vote count to the text file
    txt_file.write("Election Results\n")
    txt_file.write("------------------------\n")
    txt_file.write("Total Votes: {total_votes}\n")
    txt_file.write("------------------------\n")
    # Loop through the candidates to determine vote percentages and identify the winner
    for candiate in Candidates:
        #Getting the vote count for the candiate
        Votes = Candiate_votes_count[candiate]

        # Get the vote count and calculate the percentage
        Vote_Percentage = (Votes / total_votes) * 100

        # Update the winning candidate if this one has more votes
        if Votes > Winning_Votes:
            #Updating the highest number of votes received
            Winning_Votes = Votes
            #Updating the name of the winning candiate 
            Winning_Candiiate = candiate

        # Print and save each candidate's vote count and percentage
        #Saving the candiate's vote count and percentage
        Candidate_Vote_count_and_Percentage = f"{candiate}: {Vote_Percentage:.3f}% ({Votes})"
        
        print(Candidate_Vote_count_and_Percentage)
        txt_file.write(Candidate_Vote_count_and_Percentage + "\n")

    # Generate and print the winning candidate summary
    print("------------------------")
    print(f"Winner: {Winning_Candiiate}")
    print("------------------------")
    # Save the winning candidate summary to the text file
    txt_file.write("------------------------\n")
    txt_file.write(f"Winner: {Winning_Candiiate}\n")
    txt_file.write("------------------------\n")
