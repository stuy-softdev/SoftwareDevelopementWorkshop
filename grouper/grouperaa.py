# Saxon Rassner
# Devo Trio
# SoftDev
# K17 -- Back in the (NY) Groove
# 2026-09-28m

import random
import csv

"""
SEPERATION CRITERIA + APPROACH:
    1. Every entry is read from the csv file
    2. The order of the entries is shuffled
    3. Split into three equal tribes
    4. Create teams from tribes
    
""""""
HOW WE SANITIZE DATA:
    Handled by csv.DictReader
"""

# Read csv file
quackers = []
with open('handles_w_quackers.csv') as csvfile:
    quackers = csv.DictReader(csvfile)
    # Read the file completely
    quackers = [ a for a in quackers ]

# randomize order
# must be done before turning into devo: duckie format because shuffle errors on dicts
random.shuffle(quackers)

# split into groups
arrs:list[list[str]] = [quackers[::3], quackers[1::3], quackers[2::3]]

# If one person would be left alone, take another from third tribe
if len(arrs[0]) > len(arrs[1]):
    arrs[1].append(arrs[2].pop(-1))

# Put into devo: duckie format
# Q why the str(ind)+ ?
# A Some people share first names, without it, the dictionary would confuse them up
for x in range(len(arrs)):
    arrs[x] = { (str(ind)+", "+str(x)+" "+a["DEVO"]): a["DUCKIE"] for ind, a in enumerate(arrs[x]) }


print(len(arrs[0]))
print(len(arrs[1]))
print(len(arrs[2]))

print(arrs)
print("""
SEPERATION CRITERIA + APPROACH:
    1. Every entry is read from the csv file
    2. The order of the entries is shuffled
    3. Split into three equal tribes
    4. Create teams from tribes
    
""")

groups = [{} for x in range(len(arrs[0]))]

for x in range(len(arrs)):
    i = 0
    for k in arrs[x]:
        groups[i][k] = arrs[x][k]
        i += 1

print(groups)

for x in range(len(groups)):
    print("\nGroup " + str(x))
    # Q why the .strip()?
    # A To remove extra discriminating information that was left behind (see earlier).
    print("\n".join([k.strip("0123456789 ,") + ": " + v for k, v in groups[x].items()]))
