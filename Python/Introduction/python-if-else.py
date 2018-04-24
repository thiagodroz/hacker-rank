if __name__ == '__main__':
  n = int(input())

  if n % 2 == 1:
    print("Weird")
  else:
    if (n >= 2 and n < 5) or (n > 20):
      print("Not Weird")
    else:
      print("Weird")
