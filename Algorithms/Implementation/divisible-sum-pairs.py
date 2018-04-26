#!/bin/python3

import sys

def divisibleSumPairs(n, k, ar):
    number_of_pairs = 0
    
    for i in range(n - 1):
        for j in range(i + 1, n):
            if (ar[i] + ar[j]) % k == 0:
                number_of_pairs += 1
                    
    return number_of_pairs
                

n, k = input().strip().split(' ')
n, k = [int(n), int(k)]
ar = list(map(int, input().strip().split(' ')))
result = divisibleSumPairs(n, k, ar)
print(result)
