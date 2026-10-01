"""
Saxon Rassner
Devo Trio
SoftDev
K11 -- Reviewing python basics
2026-09-17r
time spent: 0.044
"""

"""
Given a string and a non-negative int n, we'll say that the front of the string is the first 3 chars, or whatever is there if the string is less than length 3. Return n copies of the front;

front_times('Chocolate', 2) → 'ChoCho'
front_times('Chocolate', 3) → 'ChoChoCho'
front_times('Abc', 3) → 'AbcAbcAbc'
"""

def front_times(str, n):
    if len(str) <= 3:
        return str * n
    else:
        return str[:3] * n
    
front_times('Chocolate', 2) # --> 'ChoCho'	'ChoCho'	OK	
front_times('Chocolate', 3) # --> 'ChoChoCho'	'ChoChoCho'	OK	
front_times('Abc', 3) # --> 'AbcAbcAbc'	'AbcAbcAbc'	OK	
front_times('Ab', 4) # --> 'AbAbAbAb'	'AbAbAbAb'	OK	
front_times('A', 4) # --> 'AAAA'	'AAAA'	OK	
front_times('', 4) # --> ''	''	OK	
front_times('Abc', 0) # --> ''	''	OK	