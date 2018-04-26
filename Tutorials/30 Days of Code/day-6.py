n = int(input())

for x in range(0, n):
  string = input()
  
  even = ''
  odd = ''
  
  for i in range(len(string)):
    if i % 2 == 0:
      even += string[i]
    else:
      odd += string[i]
      
  print(even + ' ' + odd)