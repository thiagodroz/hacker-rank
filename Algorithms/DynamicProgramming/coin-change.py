#!/bin/python3


def getWays(n, coins):
  combinations = [0 for _ in range(n + 1)]
  combinations[0] = 1

  for coin in coins:
    for i in range(1, len(combinations)):
      if i >= coin:
        combinations[i] += combinations[i - coin]

  return combinations[len(combinations) - 1]

nm = input().split()
n = int(nm[0])
m = int(nm[1])
c = list(map(int, input().split()))
print(getWays(n, c))
