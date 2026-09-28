"""
Saxon Rassner
Devo Trio
SoftDev
K11 -- Reviewing python basics
2026-09-17r
time spent: 0.023
"""

"""
Given a non-empty string like "Code" return a string like "CCoCodCode".

string_splosion('Code') → 'CCoCodCode'
string_splosion('abc') → 'aababc'
string_splosion('ab') → 'aab'
"""

def string_splosion(str):
    ret = ""
    
    for x in range(len(str)):
        ret += str[:x+1]
        
    return ret

string_splosion('Code') # --> 'CCoCodCode'	'CCoCodCode'	OK	
string_splosion('abc') # --> 'aababc'	'aababc'	OK	
string_splosion('ab') # --> 'aab'	'aab'	OK	
string_splosion('x') # --> 'x'	'x'	OK	
string_splosion('fade') # --> 'ffafadfade'	'ffafadfade'	OK	
string_splosion('There') # --> 'TThTheTherThere'	'TThTheTherThere'	OK	
string_splosion('Kitten') # --> 'KKiKitKittKitteKitten'	'KKiKitKittKitteKitten'	OK	
string_splosion('Bye') # --> 'BByBye'	'BByBye'	OK	
string_splosion('Good') # --> 'GGoGooGood'	'GGoGooGood'	OK	
string_splosion('Bad') # --> 'BBaBad'	'BBaBad'	OK	