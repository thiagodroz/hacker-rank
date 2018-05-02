#!/bin/python3


def factorial(n):
  if n == 1:
    return 1
  return n * factorial(n - 1)

n = int(input().strip())
print(str(factorial(n)))
