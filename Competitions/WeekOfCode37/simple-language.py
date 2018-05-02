#!/bin/python3


def maximumProgramValue(n):
  result = 0

  for _ in range(n):
    command, value = input().split(' ')

    if command == 'set':
      new_value = int(value)

      if new_value > result:
        result = new_value
    elif command == 'add':
      value_to_sum = int(value)

      if value_to_sum > 0:
        result += value_to_sum

  return result


n = int(input())
print(maximumProgramValue(n))
