#!/bin/python3

import sys


t = int(input().strip())
for a0 in range(t):
    N = int(input().strip())
    print(sum(d != 0 and N % d == 0 for d in map(int, str(N))))
