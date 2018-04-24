#!/bin/python3

import sys


n = int(input().strip())
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]

result = ""

for x in range(len(arr) - 1, -1, -1):
  result += str(arr[x]) + " "

print(result)
