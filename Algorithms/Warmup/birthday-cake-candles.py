#!/bin/python3

import sys

def birthdayCakeCandles(n, ar):
  biggest = 0
  
  for x in range(0, n):
    if ar[x] > biggest:
      biggest = ar[x]
      result = 1
    elif ar[x] == biggest:
      result += 1
      
  return result

n = int(input().strip())
ar = list(map(int, input().strip().split(' ')))
result = birthdayCakeCandles(n, ar)
print(result)
