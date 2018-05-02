#!/bin/python3
import sys


t = int(input().strip())
for a0 in range(t):
  b, w = input().strip().split(' ')
  b, w = [int(b), int(w)]
  x, y, z = input().strip().split(' ')
  x, y, z = [int(x), int(y), int(z)]
  if x + z < y:
    print (x * b + w * (x + z))
  elif y + z < x:
    print (y * w + b * (y + z))
  else:
    print (x * b + y * w)
