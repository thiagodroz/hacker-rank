#!/bin/python3

import sys


n = int(input().strip())
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]

result = ""

for x in range(len(arr) - 1, -1, -1):
  result += str(arr[x]) + " "

print(result)

# ------------ New Solution ------------------
#!/bin/python3


def reverseArray(a):
  return [a[len(a) - x - 1] for x in range(len(a))]


arr_count = int(input())
arr = list(map(int, input().split()))
res = reverseArray(arr)

print(' '.join(map(str, res)))
