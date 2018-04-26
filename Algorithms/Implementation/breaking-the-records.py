#!/bin/python3

import sys

def getRecord(s):
    max_score = s[0]
    max_score_increments = 0
    min_score = s[0]
    min_score_decrements = 0
    
    for score in s:
        if score > max_score:
            max_score = score
            max_score_increments += 1
        else:
            if score < min_score:
                min_score = score
                min_score_decrements += 1
                
    return [max_score_increments, min_score_decrements]
            

n = int(input().strip())
s = list(map(int, input().strip().split(' ')))
result = getRecord(s)
print (" ".join(map(str, result)))
