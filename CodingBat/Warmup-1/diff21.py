# Saxon "Liberty" Rassner
# Developing Trio
# SoftDev
# K11 -- Reviewing python basics
# 2026-09-18f
# time spent: 0.083hr

def diff21(n):
    if n >= 21:
        return 2 * (n - 21)
    else:
        return 21 - n
    
print(diff21(19))
print(diff21(10))
print(diff21(21))
print(diff21(-10))
print(diff21(100))