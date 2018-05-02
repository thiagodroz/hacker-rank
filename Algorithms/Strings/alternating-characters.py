#!/bin/python3
import sys


def alternatingCharacters(s):
  deletes = 0

  for i in range(1, len(s)):
    if s[i] == s[i - 1]:
      deletes += 1

  return deletes


q = int(input().strip())
for _ in range(q):
  s = input().strip()
  result = alternatingCharacters(s)
  print(result)
