n = int(input())
arr = list(map(int, input().split()))

first = max(arr)

while max(arr) == first:
    arr.remove(max(arr))

print(max(arr))
