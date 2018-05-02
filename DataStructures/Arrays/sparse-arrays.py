s = int(input())
strings = []

for _ in range(0, s):
  strings.append([input()])

q = int(input())

for _ in range(0, q):
  results = 0
  query = input()
  for search in strings:
    if query in search:
      results += 1

  print(results)
