#!/bin/python3

input()
print(sum(c * 2 ** j for (j, c)
          in enumerate(sorted(map(int, input().split()), reverse=True))))
