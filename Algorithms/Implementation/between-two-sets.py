#!/bin/python3

import sys

def getTotalX(a, b):
    total = 0
    
    for n in range(1, b[0] + 1):
      fail = False
      
      for _a in a:
        if n % _a != 0:
          fail = True
          break
          
      if not fail:
        for _b in b:
          if _b % n != 0:
            fail = True
            break
            
      if not fail:
        total = total + 1
    
    return total

if __name__ == "__main__":
    n, m = input().strip().split(' ')
    n, m = [int(n), int(m)]
    a = list(map(int, input().strip().split(' ')))
    b = list(map(int, input().strip().split(' ')))
    total = getTotalX(a, b)
    print(total)
