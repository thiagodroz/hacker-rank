#!/bin/python3


def gameWithCells(n, m):
  return (n + n % 2) * (m + m % 2) // 4


nm = input().split()
n = int(nm[0])
m = int(nm[1])
result = gameWithCells(n, m)
print(result)
