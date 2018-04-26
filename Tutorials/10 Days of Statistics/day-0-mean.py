n = int(input())
arr = list(map(int, input().split(' ')))
arr.sort()

mean = 0
number_dict = dict()

for number in arr:
  mean += number
  
  if number in number_dict:
    number_dict[number] = number_dict[number] + 1
  else:
    number_dict[number] = 1
  
mean /= n

print(mean)

if n % 2 == 0:
  print((arr[int(n/2)]+arr[int((n/2)-1)])/2)
else:
  print(arr[int(n/2)-1])

biggest_count = 0
mode = 0

for number in arr:
  if number_dict[number] > biggest_count:
    biggest_count = number_dict[number]
    mode = number
    
print(mode)