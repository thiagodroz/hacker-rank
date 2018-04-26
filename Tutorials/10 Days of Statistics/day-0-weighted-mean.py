n = input()
x = list(map(int, input().split(' ')))
w = list(map(int, input().split(' ')))

sum = 0
divider = 0

for i in range (0, len(x)):
  sum += x[i] * w[i]
  divider += w[i]

result = sum / divider
print(format(result, '.1f'))