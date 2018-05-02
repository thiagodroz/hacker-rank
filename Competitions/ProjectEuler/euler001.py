#!/bin/python3
import sys


def sum_of_divisible_by(n, p):
  if n > p:
    return 0

  while not (p % n == 0):
    p -= 1

  N = p // n

  return (N + 1) * N // 2 * n


t = int(input().strip())
for _ in range(t):
  n = int(input().strip())

  result = 0

  result += sum_of_divisible_by(3, n - 1)
  result += sum_of_divisible_by(5, n - 1)
  result -= sum_of_divisible_by(15, n - 1)

  print(result)
