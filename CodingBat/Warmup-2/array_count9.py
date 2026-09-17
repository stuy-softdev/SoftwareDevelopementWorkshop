"""
Batuhan Sekeroglu
Devo Trio
SoftDev
K11 -- Reviewing python basics
2026-09-17r
time spent: 0.014
"""

"""
Given an array of ints, return the number of 9's in the array.

array_count9([1, 2, 9]) # --> 1
array_count9([1, 9, 9]) # --> 2
array_count9([1, 9, 9, 3, 9]) # --> 3
"""

def array_count9(nums):
    ret = 0
    
    for x in nums:
        if x == 9:
            ret += 1arra
            
    return ret

array_count9([1, 2, 9]) # --> 1	1	OK	
array_count9([1, 9, 9]) # --> 2	2	OK	
array_count9([1, 9, 9, 3, 9]) # --> 3	3	OK	
array_count9([1, 2, 3]) # --> 0	0	OK	
array_count9([]) # --> 0	0	OK	
array_count9([4, 2, 4, 3, 1]) # --> 0	0	OK	
array_count9([9, 2, 4, 3, 1]) # --> 1	1	OK	