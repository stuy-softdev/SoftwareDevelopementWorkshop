"""
Saxon Rassner
Devo Trio
SoftDev
K11 -- Reviewing python basics
2026-09-17r
time spent: 0.027
"""

"""
Given a string, return a new string made of every other char starting with the first, so "Hello" yields "Hlo".

string_bits('Hello') → 'Hlo'
string_bits('Hi') → 'H'
string_bits('Heeololeo') → 'Hello'
"""

def string_bits(str):
    ret = ""
    
    for x in range(len(str)):
        if x % 2 == 0:
            ret += str[x]
            
    return ret

string_bits('Hello') # --> 'Hlo'	'Hlo'	OK	
string_bits('Hi') # --> 'H'	'H'	OK	
string_bits('Heeololeo') # --> 'Hello'	'Hello'	OK	
string_bits('HiHiHi') # --> 'HHH'	'HHH'	OK	
string_bits('') # --> ''	''	OK	
string_bits('Greetings') # --> 'Getns'	'Getns'	OK	
string_bits('Chocoate') # --> 'Coot'	'Coot'	OK	
string_bits('pi') # --> 'p'	'p'	OK	
string_bits('Hello Kitten') # --> 'HloKte'	'HloKte'	OK	
string_bits('hxaxpxpxy') # --> 'happy'	'happy'	OK