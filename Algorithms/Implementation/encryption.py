#!/bin/python3
import sys
from math import ceil, sqrt


s = input().strip()
c = ceil(sqrt(len(s)))
print(' '.join(map(lambda x: s[x::c], range(c))))
