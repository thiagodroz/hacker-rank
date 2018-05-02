#!/bin/python3
import sys


T = int(input().strip())
for _ in range(T):
  N = int(input().strip())
  if N <= 1:
    print(0)
  else:
    print(int((N * (N-1)) / 2))
