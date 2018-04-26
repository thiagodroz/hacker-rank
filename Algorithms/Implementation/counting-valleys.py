n = int(input())
steps = input()

current_level = 0
number_of_valleys = 0

for step in steps:
    if step == "D":
        current_level -= 1
        
    elif step == "U":
        current_level += 1
        
        if current_level == 0:
            number_of_valleys += 1
        
print(number_of_valleys)
