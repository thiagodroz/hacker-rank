#!/bin/python3


def totalForecastInaccuracy(t, f):
  sum_of_inaccuracies = 0

  for i in range(len(t)):
    sum_of_inaccuracies += abs(t[i] - f[i])

  return sum_of_inaccuracies


t = list(map(int, input().split()))
f = list(map(int, input().split()))

result = totalForecastInaccuracy(t, f)

print(result)
