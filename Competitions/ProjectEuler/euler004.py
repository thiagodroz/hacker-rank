#!/bin/python3
import sys


def is_palindrome(n):
  s = str(n)
  return s == s[::-1]


def biggest__product_below_n(n):
  max_in_n = 0
  for x in range(999, 99, -1):
    for y in range(999, x-1, -1):
      product = x * y

      if product > n:
        continue
      if product <= max_in_n:
        break

      if is_palindrome(product) and product < n:
        max_in_n = product

  return max_in_n


t = int(input().strip())

for _ in range(t):
    n = int(input().strip())
    print(biggest__product_below_n(n))
