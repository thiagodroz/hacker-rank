#!/bin/python3

import sys

arr = list(map(int, input().strip().split(' ')))

sum = 0
max = 0

for x in arr:
  sum += x
  
min = sum
  
for x in arr:
  current = sum - x
  if current > max:
    max = current
  if current < min:
    min = current
    
print(str(min) + " " + str(max))