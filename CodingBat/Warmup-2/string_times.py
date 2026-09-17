"""
Batuhan Sekeroglu
Devo Trio
SoftDev
K11 -- Reviewing python basics
2026-09-16w
time spent: 0.3
"""

"""
Given a string and a non-negative int n, return a larger string that is n copies of the original string.

string_times('Hi', 2) → 'HiHi'
string_times('Hi', 3) → 'HiHiHi'
string_times('Hi', 1) → 'Hi'
"""

def string_times(str, n):
    st = ""
    for x in range(n):
        st += str
        
    return st

string_times('Hi', 2) # --> 'HiHi'	'HiHi'	OK	
string_times('Hi', 3) # --> 'HiHiHi'	'HiHiHi'	OK	
string_times('Hi', 1) # --> 'Hi'	'Hi'	OK	
string_times('Hi', 0) # --> ''	''	OK	
string_times('Hi', 5) # --> 'HiHiHiHiHi'	'HiHiHiHiHi'	OK	
string_times('Oh Boy!', 2) # --> 'Oh Boy!Oh Boy!'	'Oh Boy!Oh Boy!'	OK	
string_times('x', 4) # --> 'xxxx'	'xxxx'	OK	
string_times('', 4) # --> ''	''	OK	
string_times('code', 2) # --> 'codecode'	'codecode'	OK	
string_times('code', 3) # --> 'codecodecode'	'codecodecode'	OK