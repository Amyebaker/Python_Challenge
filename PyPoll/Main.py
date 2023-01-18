import os
import csv
election_path = os.path.join('.','PyPoll', 'Resources', 'election_data.csv')
election_results = os.path.join ('.', 'PyPoll','Analysis','election_results.txt')
candidates ={}
total_votes=0
with open(election_path) as election_file:
    election_reader = csv.reader(election_file, delimiter=',')
    csv_header = next(election_reader)

    for row in election_reader:
        voter_ID = row[0]
        county = row[1]
        candidate = row[2]

        total_votes = total_votes + 1
        if candidate in candidates:
            votes = candidates[candidate] + 1
            update_candidate = {candidate: votes}
            candidates.update(update_candidate)
        else:
            candidates.update({candidate: 1})

write_file = open(election_results, 'w')
print("Election Results")
print("----------------------------")
write_file.write(f"Election Results\n")
write_file.write(f"----------------------------\n")
print(f"Total Votes: {total_votes}")
print("----------------------------")
write_file.write(f"Total Votes: {total_votes}\n")
write_file.write(f"----------------------------\n")

most_votes = 0
for candidate, votes in candidates.items():
    vote_percentage = "{:.3f}".format(votes / total_votes * 100)
    if votes > most_votes:
        most_votes = votes
        winner = candidate

    
    print(f"{candidate}: {vote_percentage}% ({votes})")

    write_file.write(f"{candidate}: {vote_percentage}% ({votes})\n")

print("----------------------------")
print(f"Winner: {winner}")
print("----------------------------")

write_file.write(f"----------------------------\n")
write_file.write(f"Winner: {winner}\n")
write_file.write(f"----------------------------\n")

write_file.close()