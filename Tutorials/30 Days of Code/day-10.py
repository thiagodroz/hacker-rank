#!/bin/python3

import sys


n = int(input().strip())
binary = ""

while n > 1:
  binary += str(n % 2)
  n = n // 2

binary += str(n % 2)

currentSequence = 0
biggestSequence = 0
for char in binary:
  if char == "1":
    currentSequence += 1
    if currentSequence > biggestSequence:
      biggestSequence = currentSequence
  else:
    currentSequence = 0
    
    
print(biggestSequence)
