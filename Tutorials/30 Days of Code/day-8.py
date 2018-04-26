n = int(input())
arr = dict()

for i in range(0, n):
  entries = input().split(' ')
  arr[entries[0]] = entries[1]
  
query = input()
  
while query != "":
  if query in arr:
    print(query + "=" + arr[query])
  else:
    print("Not found")
  
  query = input()