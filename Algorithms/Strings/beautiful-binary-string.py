#!/bin/python3
import sys


def beautifulBinaryString(b):
  steps = 0
  s = str(b)

  while "010" in s:
    i = s.index("010")
    s = s[:i + 2] + "1" + s[i + 3:]
    steps += 1

  return steps


if __name__ == "__main__":
  n = int(input().strip())
  b = input().strip()
  result = beautifulBinaryString(b)
  print(result)
