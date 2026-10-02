import sys
import random

"""
Saxon Rassner
Devo Trio
SoftDev
K14 -- Grab Bag
2026-09-22t - 2026-09-23w
"""

"""
grouper.py
Reads a file and splits it into three
"""
"""
First, the pool is split into its constituent lines. These lines are then
divided into three groups of roughly equal size by first creating the three
buckets that will hold the result. First, a random element is added into the
first bucket, then the next, then the third before going back to the first.
"""

"""
Data sanitization occurs naturally because the file.read() function turns the
file into a string. Our program only operates on string functions with no
regard for its actual content besides '\n's for splitting the string. BUT, a
file ends in a \n as well, causing extraneous lines. This gets removed with a
[:-1].
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

# Randomize start position
start = random.randint(0, len(splitted)-1)

arrs = [[], [], []]

cur_arr = 0

while len(splitted) > 0:
    arrs[cur_arr].append(splitted.pop(random.randint(0, len(splitted)-1)))
    cur_arr = (cur_arr+1) % 3

# print the result
print(arrs)
# and an explanation of the criteria used to divide the pool
print("""
First, the pool is split into its constituent lines. These lines are then
divided into three groups of roughly equal size by first creating the three
buckets that will hold the result. First, a random element is added into the
first bucket, then the next, then the third before going back to the first.
""")

# print groups

for x in range(len(arrs[0])):
    print("\nGroup " + str(x))
    print(arrs[0][x])
    if x < len(arrs[1]):
        print(arrs[1][x])
    if x < len(arrs[2]):
        print(arrs[2][x])
