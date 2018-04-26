#!/bin/python3

for p in range(int(input())):
    x,y,z = map(int,input().split())
    print("Cat A" if abs(z - x) < abs(z - y) else "Cat B" if abs(z - x) > abs(z - y) else "Mouse C")
