#!/bin/python3

import sys

def get_hourglass_values(arr, x, y):
  hourglass = []
  
  for i in range(x, x + 3):
    for j in range(y, y + 3):
      hourglass.append(arr[i][j])
      
  hourglass.pop(5)
  hourglass.pop(3)
  
  return hourglass

arr = []
for arr_i in range(6):
   arr_t = [int(arr_temp) for arr_temp in input().strip().split(' ')]
   arr.append(arr_t)
  
biggest_sum = None

for x in range(0, 4):
  for y in range(0, 4):
    hourglass = get_hourglass_values(arr, x, y)
    
    hourglass_sum = 0
    for value in hourglass:
      hourglass_sum += int(value)
      
    if biggest_sum is None or hourglass_sum > biggest_sum:
      biggest_sum = hourglass_sum

print(str(biggest_sum))
