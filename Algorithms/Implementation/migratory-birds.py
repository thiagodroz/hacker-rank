#!/bin/python3

import sys

def migratoryBirds(n, ar):
    number_of_birds = dict((el, 0) for el in ar)
    
    for bird in ar:
        number_of_birds[bird] += 1
        
    bird_result = ar[0]
    bird_number = 0
    
    for bird, number in number_of_birds.items():
        if number > bird_number:
            bird_number = number
            bird_result = bird
            
    return bird_result

n = int(input().strip())
ar = list(map(int, input().strip().split(' ')))
result = migratoryBirds(n, ar)
print(result)
