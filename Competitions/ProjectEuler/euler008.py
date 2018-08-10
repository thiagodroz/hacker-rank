#!/bin/python3
from functools import reduce
import operator


def largest_product(num, digits):
  largest = 0
  
  for i in range(len(num) - digits - 1):
    current = reduce(operator.mul, list(map(int, num[i:(i + digits)])))
    
    if current > largest:
      largest = current
  
  return largest
    
    
t = int(input().strip())
for _ in range(t):
  n, k = input().strip().split(' ')
  n, k = [int(n),int(k)]
  num = input().strip()
  print(largest_product(num, k))
