#!/bin/python3
import sys
from math import gcd
from functools import reduce


t = int(input().strip())

for _ in range(t):
  n = int(input().strip())

  print(reduce(lambda x, y: x * y // gcd(x, y), range(1, n + 1)))
