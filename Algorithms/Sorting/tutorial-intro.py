v = input()
n = int(input())
arr = input().strip().split(' ')

for i in range(n):
  if arr[i] == v:
    print(i)
    break
