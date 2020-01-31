# Add dependencies.
import csv
import os

# Assign a variable to load election results file from a path.
file_to_load = os.path.join("Resources/election_results.csv")

# Assign a variable to save the output file to a path.
file_to_save = os.path.join("Analysis", "election_analysis.txt")

# Initialize a total vote counter.
total_votes = 0

# Declare List for Candidates and dictionary for candidate votes.
candidate_options = []
candidate_votes = {}

# Declare List for counties and dictionary for votes by county.
county_options = []
county_votes = {}

# Declare variables to track the winning candidate,
# vote count, and percentage.
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Declare variables to track the county with the largest turnout.
top_county_turnout = ""
largest_count = 0

# Open the election results and read the file.
with open(file_to_load) as election_data:
    
    file_reader = csv.reader(election_data)
    
    # Read the header row.
    headers = next(file_reader)
    
    # Cycle through each row in the CSV file.
    for row in file_reader:
        
        # Add to the total vote count.
        total_votes += 1
        
        # Get the county name from each row.
        county_name = row[1]
        
        # If the county does not match any existing county, add to
        # the county list.
        if county_name not in county_options:
            
            # Add the county name to the county list.
            county_options.append(county_name)
            
            # And begin tracking that county's voter count.
            county_votes[county_name] = 0
        
        # Add a vote to that county's count.
        county_votes[county_name] += 1
        
        # Get the candidate name from each row.
        candidate_name = row[2]
        
        # If the candidate does not match any existing candidate, add to
        # the candidate list.
        if candidate_name not in candidate_options:
            
            # Add the candidate name to the candidate list.
            candidate_options.append(candidate_name)
            
            # And begin tracking that candidate's voter count.
            candidate_votes[candidate_name] = 0
        
        # Add a vote to that candidate's count.
        candidate_votes[candidate_name] += 1

# Save the results to text file.
with open(file_to_save, "w") as txt_file:
    
    # Print the final vote count to the terminal.
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
    print(election_results, end="")
    
    # Save the results to the text file.
    txt_file.write(election_results)
    
    # Save the final vote count by county to the text file
    for county in county_votes:
        
        # Retrieve vote count and percentage.
        votes_county = county_votes[county]
        vote_percentage_county = float(votes_county) / float(total_votes) * 100
        county_results = (
            f"{county}: {vote_percentage_county:.1f}% ({votes_county:,})\n")

        # Print each county's voter count and percentage to the terminal.
        print(county_results)
        
        #  Save the county results to the text file.
        txt_file.write(county_results)
        
        # Determine largest vote count for the counties.
        if (votes_county > largest_count):
            largest_count = votes_county
            top_county_turnout = county
                
    # Print the larget county turnout to the terminal.
    largest_county_summary = (
        f"-------------------------\n"
        f"Largest County Turnout: {top_county_turnout}\n"
        f"-------------------------\n")
    print(largest_county_summary)
    
    # Save the largest county summary to the text file.
    txt_file.write(largest_county_summary)
    
    # Save the final vote count by candidate to the text file.
    for candidate in candidate_votes:
        
        # Retrieve vote count and percentage.
        votes = candidate_votes[candidate]
        vote_percentage = float(votes) / float(total_votes) * 100
        candidate_results = (
            f"{candidate}: {vote_percentage:.1f}% ({votes:,})\n")

        # Print each candidate's voter count and percentage to the terminal.
        print(candidate_results)
        
        # Save the candidate results to the text file.
        txt_file.write(candidate_results)
        
        # Determine winning vote count, winning percentage, and winning candidate.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_candidate = candidate
            winning_percentage = vote_percentage
    
    # Print the winning candidate's results to the terminal.
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary)
    
    # Save the winning candidate's results to the text file.
    txt_file.write(winning_candidate_summary)

# Close the data file
election_data.close()

# Close the results file
txt_file.close()


