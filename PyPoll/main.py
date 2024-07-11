import os
import csv

csvpath = os.path.join("Resources", "election_data.csv")

vote_count = []
candidates = set()

total_votes = 0
stockham_votes = 0
degette_votes = 0
doane_votes = 0

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)

# The total number of votes cast
    for row in csvreader:
        total_votes += 1

# A complete list of candidates who received votes
        candidate = row[2]
        candidates.add(candidate)

# The total number of votes each candidate won
        if candidate == "Charles Casper Stockham":
            stockham_votes += 1
            
        elif candidate == "Diana DeGette":
            degette_votes += 1

        elif candidate == "Raymon Anthony Doane":
            doane_votes += 1

# The percentage of votes each candidate won
stockham_per = (stockham_votes) / (total_votes) * 100
degette_per = (degette_votes) / (total_votes) * 100
doane_per = (doane_votes) / (total_votes) * 100

# The winner of the election based on popular vote
if stockham_votes > degette_votes and stockham_votes > doane_votes:
    winner = "Charles Casper Stockham"
elif degette_votes > stockham_votes and degette_votes > doane_votes:
    winner = "Diana DeGette"
elif doane_votes > stockham_votes and doane_votes > degette_votes:
    winner = "Raymon Anthony Doane"
print(winner)

# analysis
analysis = (
    "Election Results\n"
    "-------------------------\n"
    f"Total Votes: {total_votes}\n"
    "-------------------------\n"
    f"Charles Casper Stockham: {stockham_per:.3f}% ({stockham_votes})\n"
    f"Diana DeGette: {degette_per:.3f}% ({degette_votes})\n"
    f"Raymon Anthony Doane: {doane_per:.3f}% ({doane_votes})\n"
    "-------------------------\n"
    f"Winner: {winner}\n"
    "-------------------------\n"
)
print(analysis)

# Export the analysis to .txt
with open('poll_analysis.txt', 'w') as file:
    file.write(analysis)