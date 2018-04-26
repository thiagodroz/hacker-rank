quantity = int(input())

def is_prime(n):
    if n == 2:
        return "Prime"
    
    if n < 2 or n % 2 == 0:
        return "Not prime"
    
    m = 3
    
    while m ** 2 <= n:
        if n % m == 0:
            return "Not prime"
        
        m += 2
        
    return "Prime"
    

for x in range(quantity):
    n = int(input())
    
    print(is_prime(n))