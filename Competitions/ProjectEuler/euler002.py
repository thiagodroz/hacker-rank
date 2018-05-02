#!/bin/python3
import sys


t = int(input().strip())
for _ in range(t):
  n = int(input().strip())

  previous = 1
  current = 2
  fibo_sum = 0

  while current <= n:
    if current % 2 == 0:
      fibo_sum += current

    current += previous
    previous = current - previous

  print(fibo_sum)
