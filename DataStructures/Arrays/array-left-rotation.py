#!/bin/python3


def rotate_array(rotates, arr):
  start = arr[0:rotates]
  end = arr[rotates:]

  return end + start


nd = input().split()
n = int(nd[0])
d = int(nd[1])

a = list(map(str, input().split()))
result = rotate_array(d, a)

print(' '.join(result))
