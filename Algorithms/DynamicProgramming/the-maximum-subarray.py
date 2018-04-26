n = int(input())

def find_biggest_number(array):
  result = array[0]
  for element in array:
    if element > result:
      result = element
      
  return result

def find_max_contiguous_subarray(array):
  current_sum = 0
  biggest_sum = 0
  contiguous_sum = 0
  done = False
  
  for element in array:
    if element > 0:
      if contiguous_sum + element > element:
        current_sum = contiguous_sum + element
        contiguous_sum = current_sum
      else:
        current_sum = element
        contiguous_sum = element
    else:
      contiguous_sum += element
      current_sum = 0
      
    if current_sum > biggest_sum:
      biggest_sum = current_sum
      done = True
      
  if done:
    return biggest_sum
  else:
    return find_biggest_number(array)
  
def find_max_non_contiguous_subarray(array):
  result = 0
  done = False
  for element in array:
    if element > 0:
      result += element
      done = True
      
  if done:
    return result
  else:
    return find_biggest_number(array)

for x in range(0, n):
  m = input()
  array = list(map(int, input().split(' ')))
  
  result = str(find_max_contiguous_subarray(array))
  result += " "
  result += str(find_max_non_contiguous_subarray(array))
  
  print(result)
  