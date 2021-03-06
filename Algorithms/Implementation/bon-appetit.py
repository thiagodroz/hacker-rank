#!/bin/python3
import sys

def bonAppetit(n, k, b, ar):
    annaBill = sum(ar[i] for i in range(n) if i != k)//2
    return 'Bon Appetit' if annaBill == b else str(b-annaBill)

n, k = input().strip().split(' ')
n, k = [int(n), int(k)]
ar = list(map(int, input().strip().split(' ')))
b = int(input().strip())
result = bonAppetit(n, k, b, ar)
print(result)
