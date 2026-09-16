# Saxon "Liberty" Rassner
# Developing Trio
# SoftDev
# K11 -- Reviewing python basics
# 2026-09-18f
# time spent: 0.083hr

def parrot_trouble(talking, hour):
    if hour >= 7 and hour <= 20:
        return False
    elif talking == True:
        return True
    else:
        return False
    
print(parrot_trouble(True, 5))
print(parrot_trouble(True, 9))
print(parrot_trouble(True, 23))
print(parrot_trouble(False, 5))
print(parrot_trouble(False, 9))
print(parrot_trouble(False, 23))
        