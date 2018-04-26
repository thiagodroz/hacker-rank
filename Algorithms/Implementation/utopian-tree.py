#!/bin/python3

import sys

def growthCycle(x):
    if x == 0:
        h = 1
    elif x % 2 == 0:
        h = 2 ** ((x/2) + 1) - 1
    elif x % 2 == 1:
        h = 2 ** ((x + 3)/2) - 2
    return h

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    res = int(growthCycle(n))
    print(res)
