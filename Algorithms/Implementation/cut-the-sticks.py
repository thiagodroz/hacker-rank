#!/bin/python3
import sys

n = int(input())
stick = sorted(list((map(int, input().split(" ")))))

while(len(stick) > 0):
  print(len(stick))
  stick = list(filter(lambda y: y > 0, list(
    filter(lambda x: x - min(stick), stick))))
