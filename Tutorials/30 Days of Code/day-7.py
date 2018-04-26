#!/bin/python3

import sys


n = int(input().strip())
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]

reversed = ""

for i in range(len(arr) - 1, -1, -1):
  reversed += str(arr[i]) + " "
  
print(reversed)