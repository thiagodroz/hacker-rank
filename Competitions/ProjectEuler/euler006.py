#!/bin/python3
import sys


t = int(input().strip())

for _ in range(t):
  n = int(input().strip())

  square_sums = (n * (n + 1) / 2) ** 2
  sum_squares = ((n + 1) * (2 * n + 1) / 6) * n

  print(int(square_sums - sum_squares))
