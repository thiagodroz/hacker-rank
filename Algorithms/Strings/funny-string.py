#!/bin/python3
import sys

for _ in range(int(input())):
  N = input()
  S = N[::-1]
  print('Funny' if all((abs(ord(N[i]) - ord(N[i - 1])) == abs(
    ord(S[i]) - ord(S[i - 1]))) for i in range(1, len(N))) else 'Not Funny')
