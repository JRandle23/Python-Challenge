print("Election Results")
print("--------------------------")

import os
import csv

csvpath = 'PyPoll/Resources/election_data.csv'

candidates = []
voter_id = []

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    header = next(csvreader)

    for row in csvreader:

        voter_id.append(row[0])
        candidates.append(row[2])

    for totalvotes in voter_id:
        totalvotes = len(voter_id)

        print("Total Votes: ", totalvotes)
        print("--------------------------")

        break
    
    from collections import Counter
    c = Counter(candidates)
    print(c)
    


   




    
   
   










