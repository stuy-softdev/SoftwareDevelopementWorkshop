# Saxon Rassner
# Strawberry Shortcake
# SoftDev
# K14 -- Grab bag
# 2026-09-23r

import random

"""
SEPERATION CRITERIA + APPROACH:
    1. We sorted by alphanumberic order (done by .find() with the first character of each handle on a string going from low to high). We
used this approach since the normal .sort() on the list places all uppercase characters before lowercase ones, and we wanted a custom
alphanumeric ordering.
    2. We split up this sorted list into thirds (first third, middle third, and last third). This was done with a table lookup.
    3. We then shuffled the groups in order to satisfy the randomized seperation requirement
    4. We then selected the teams by index:
    (team1 consists of the 1st person in group0, the 1st person in group1, the 1st person in group2,
    team2 consists of the 2nd person in group0, the 2nd person in group1, the 2nd person in group2,
   
""""""
HOW WE SANITIZE DATA:
    We basically just remove the newline at the end and call it a day
"""

# Reads a file and returns the content as a string
def readFile(filename):
    file = open(filename, 'r')
    content = file.read()
    file.close()
    return content[:-1]

# Splits the given string by newlines and returns the result as a list
def splitLine(content):
    return content.split("\n")

# read the given plaintext file,
cont = readFile("handles_gh")

# split the entries using critera of your choosing (height),
splitted = splitLine(cont)

teamSize:float = len(splitted) / 3
groups:list[list[str]] = [[], [], []]

"""process into groups"""
# sort by alphanumeric order
ALPHANUMERIC_ORDER:str = "0123456789AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz"
splitted.sort(key = lambda s: ALPHANUMERIC_ORDER.find(s[:1]))

# split into groups
for index, line in enumerate(splitted):
    groups[int(index / teamSize)].append(line)

# shuffle
for group in groups:
    random.shuffle(group)
   
"""print groups"""
print("GROUPS:")
for group in groups:
    print(group, len(group))

print("""
    We decided to sort the lists by alphanumeric order, and then split the first third, second third, and last third into seperate groups,
and then shuffle the 3 groups at the end to satisfy the "Each run of your script should produce new random selections" part of the requirements.
""")

def splitTeams(nList, m):
    names = nList.copy()
   
    length = len(names)
   
    if length < 1 or m < 1:
        return names
   
    names.sort(key=len)
    teams = []
    remainder = length % m
    for i in range(0, length - remainder, m):
        teams.append(names[i:i + m])

    #if there is one person left out
    if remainder == 1:
        #takes a person from the last team,
        lastTeam = teams.pop()
        #creates the last team without the person and adds it to the list
        teams.append(lastTeam[:-1])
        #create a new team with that person and the leftover person and adds it to the list
   
        teams.append([lastTeam[-1]] + names[length - 1:])
       
    #put leftover people into a group if remainder is 2 or more.
    elif remainder > 0:
        teams.append(names[length - remainder:])
    return teams


print(splitTeams(splitted, 3))
