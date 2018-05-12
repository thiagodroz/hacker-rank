#!/bin/python3

def gridChallenge(grid):
  for i in range(n):
    grid[i] = sorted(grid[i])
    
  for i in range(n - 1):
    for j in range(n):
      if grid[i][j]>grid[i + 1][j]:
        return "NO"
      
  return "YES"      
    

t = int(input())

for _ in range(t):
  n = int(input())
  grid = [input() for _ in range(n)]

  result = gridChallenge(grid)

  print(result)
