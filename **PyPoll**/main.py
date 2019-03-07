

import os
import csv

csvpath = os.path.join(".", "Resources", "election_data.csv")
print(csvpath)

with open(csvpath, newline = "") as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")

    candidates = []
    candidates_votes = []
    total_votes = -1
    khan_total = 0
    correy_total = 0
    li_total = 0
    tooley_total = 0

    for row in csvreader:
        total_votes += 1

        if total_votes == 0:
            continue

        if row[2] not in candidates:
            candidates.append(row[2])
            candidates_votes.append(0)

        candidates_votes[candidates.index(row[2])] += 1

print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes} ")
print("-------------------------")        

for candidate in candidates:
    cv = candidates_votes[candidates.index(candidate)]
    cp = (cv/total_votes) * 100


    print(f"{candidate}: {'{0:.3f}'.format(cp)}% ({cv})")

print("-------------------------") 
print(f"Winner: {candidates[candidates_votes.index(max(candidates_votes))]}")
print("-------------------------") 




