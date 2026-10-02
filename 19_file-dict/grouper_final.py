# Saxon Rassner
# Devo Trio
# SoftDev
# K19 -- Bring it Back Home
# 2026-10-1

import csv 
import random

tribeExplanation = """SEPARATION CRITERIA + APPROACH:
    1. We sorted the devos by alphanumeric order (done by .find() with the first character of each
name on a string going from low to high). We used this approach since the normal .sort() places all
uppercase characters before lowercase ones, and we wanted a custom alphanumeric ordering.
    2. We split this sorted list into thirds (first third, middle third, and last third). If the total
isn't divisible by 3, the first tribe(s) get one extra person, so sizes differ by at most 1.
    3. Each devo is stored with their ducky as a devo:ducky pair, so no duckie is orphaned."""

teamExplanation = """TEAM APPROACH:
    1. We shuffled each tribe so the teams are random on every run.
    2. Team 1 is the 1st person of tribe 1, tribe 2, and tribe 3; team 2 is the 2nd person of each; and so on.
So no team has more than 1 member from any tribe.
    3. If the number of devos isn't divisible by 3, the leftovers form teams of 2 (always fewer than 3 of
them), which are printed at the bottom. Each duckie is shown next to its devo."""

sanitizeExplanation = """HOW WE SANITIZE DATA:
    We remove the header line, remove any blankspace, and add (2) in the keys for duplicate names"""

# Reads a file and returns the content as a list of string lines
def readAndSplitFile(filename):
    # DANK JE WEL DEVO FAM
    with open(filename, 'r') as file:
        content = file.read().strip() # turn file into a list of individual lines
        lines = content.split("\n")
        lines.pop(0) # remove header line  
    return lines

# read the given plaintext file,
lines = readAndSplitFile("handles_w_quackers.csv")

# Creates one dictionary from the string returned from readAndSplitFile
def createDictionary(lines):
    pairs = {}
    for line in lines:
        # DANK JE WEL DEVO FAM
        if line.strip() == "":
            continue
        print(repr(line))
        parts = line.split(",", 1) # split individual line into devo and ducky
        devo = parts[0].strip()
        ducky = parts[1].strip()
        if devo in pairs:
            devo = devo + " (2)" # For the 2 andrews and ivans
        pairs[devo] = ducky
    return pairs

pairs = createDictionary(lines)
ALPHANUMERIC_ORDER:str = "0123456789AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz"

# sort dictionary
def sortPairs(devo):
    return ALPHANUMERIC_ORDER.find(devo[:1])

# split dictionary into 3 tribes with a maximum difference of 1 in size
def splitPairsIntoTribes(pairs):
    tribes = []
    names = []
    for devo in pairs:
        names.append(devo)
    
    names.sort(key = sortPairs)
    total = len(names)
    baseSize = total // 3
    size1 = baseSize
    size2 = baseSize
    size3 = baseSize
    additionalTribe = total % 3
    if (additionalTribe >= 1):
        size1 += 1
    if (additionalTribe >= 2):
        size2 += 1
        
    tribe1 = {}
    tribe2 = {}
    tribe3 = {}
    
    # DANK JE WEL DEVO FAM
    for index, devo in enumerate(names):
        if (index < size1):
            tribe1[devo] = pairs[devo]
        elif (index < size1 + size2):
            tribe2[devo] = pairs[devo]
        else:
            tribe3[devo] = pairs[devo]
    
    return [tribe1, tribe2, tribe3]

tribes = splitPairsIntoTribes(pairs)
tribe1 = tribes[0]
tribe2 = tribes[1]
tribe3 = tribes[2]

def makeTeams(tribe1, tribe2, tribe3):
    names1 = []
    for devo in tribe1:
        names1.append(devo)
    names2 = []
    for devo in tribe2:
        names2.append(devo)
    names3 = []
    for devo in tribe3:
        names3.append(devo)
        
    # randomize devos in each tribe
    random.shuffle(names1)
    random.shuffle(names2)
    random.shuffle(names3)
    smallest = len(names3)
    
    teams = []
    
    for i in range(smallest):
        team = [names1[i] +  ": " + tribe1[names1[i]], names2[i] +  ": " + tribe2[names2[i]], names3[i] +  ": " + tribe3[names3[i]]]
        teams.append(team)
        
    extra = -3 * smallest + len(names1) + len(names2) + len(names3)
    
    # add extra team if 2 left over
    if (extra == 2):
        teams.append([names1[smallest] +  ": " + tribe1[names1[smallest]], names2[smallest] +  ": " + tribe2[names2[smallest]]])
    # If only one devo remains remove the last team and combine devos such that their tribes don't overlap
    if (extra == 1):
        finalTeam = teams.pop()
        single = names1[smallest] + ": " + tribe1[names1[smallest]]
        teams.append(single, finalTeam[1])
        teams.append(finalTeam[0], finalTeam[2])
    
    return teams
    
# make teams
teams = makeTeams(tribe1, tribe2, tribe3)

# print explanations
print(tribeExplanation)
print(teamExplanation)
print(sanitizeExplanation)

# print tribes

print("Tribe 1: ", tribe1, len(tribe1))
print("Tribe 2: ", tribe2, len(tribe2))
print("Tribe 3: ", tribe3, len(tribe3))

# print teams

for index, team in enumerate(teams):
    print("Team" + str(index) + ":")
    print(team)