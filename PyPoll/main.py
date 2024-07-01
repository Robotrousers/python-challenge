import csv
from pathlib import Path

# CSV filepath
csv_path = Path("Resources/election_data.csv")

# Read CSV file
with open(csv_path, mode='r') as file:
    reader = csv.DictReader(file)
    data = list(reader)

# The total number of votes cast
total_votes = len(data)

# A complete list of candidates who received votes
candidates = list(set(row['Candidate'] for row in data))

# The percentage of votes each candidate won
candidate_votes = {candidate: 0 for candidate in candidates}

for row in data:
    candidate_votes[row['Candidate']] += 1

candidate_percentages = {candidate: (votes / total_votes) * 100 for candidate, votes in candidate_votes.items()}

# The winner of the election based on popular vote
winner = max(candidate_votes, key=candidate_votes.get)

# Prepare the analysis results
analysis = (
    "Election Results\n"
    "-------------------------\n"
    f"Total Votes: {total_votes}\n"
    "-------------------------\n"
)

for candidate in candidates:
    analysis += f"{candidate}: {candidate_percentages[candidate]:.3f}% ({candidate_votes[candidate]})\n"

analysis += "-------------------------\n"
analysis += f"Winner: {winner}\n"
analysis += "-------------------------\n"

# Export the analysis to .txt
print(analysis)
with open('poll_analysis.txt', 'w') as file:
    file.write(analysis)
