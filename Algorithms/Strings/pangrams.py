ALPHABET_SIZE = 26
chars = set(input().lower().replace(' ', ''))

if len(chars) == ALPHABET_SIZE:
    print('pangram')
else:
    print('not pangram')
