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
"""First, the pool is split into its constituent lines. These lines are
then divided into three groups of roughly equal size by first selecting a
random starting position, then putting the current line into bucket 0, next
line into bucket 1, then 2, then repeating back to 0. This is repeated until
every line in the file has been put into a bucket exactly once."""

"""
Data sanitization occurs naturally because the file.read() function turns the
file into a string. Our program only operates on string functions with no
regard for its actual content besides '\n's for splitting the string.
"""
# Reads a file and returns the content as a string
def readFile(filename):
    file = open(filename, 'r')
    content = file.read()
    file.close()
    return content

# Splits the given string by newlines and returns the result as a list
def splitLine(content):
    return content.split("\n")

# read the given plaintext file,
cont = readFile(sys.argv[1])

# split the entries using critera of your choosing (height),
splitted = splitLine(cont)

# Randomize start position
start = random.randint(0, len(splitted)-1)

# into 3 groups of as-equal-as-possible size, 
arrs = [splitted[start::3], splitted[start+1::3], splitted [start+2::3]]

# print the result
print(arrs)
# and an explanation of the criteria used to divide the pool
print("""First, the pool is split into its constituent lines. These lines are
then divided into three groups of roughly equal size by first selecting a
random starting position, then putting the current line into bucket 0, next
line into bucket 1, then 2, then repeating back to 0. This is repeated until
every line in the file has been put into a bucket exactly once.""")
