import sys

t = int(input())

for i in range(t):

    alphabet = {
        'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0,
        'h': 0, 'i': 0, 'j': 0, 'k': 0, 'l': 0, 'm': 0, 'n': 0,
        'o': 0, 'p': 0, 'q': 0, 'r': 0, 's': 0, 't': 0, 'u': 0,
        'v': 0, 'w': 0, 'x': 0, 'y': 0, 'z': 0
    }

    a = list(input().rstrip().lower())

    for char in a:
        if char in alphabet:
            alphabet[char] += 1

    min_count = min(alphabet.values())

    if min_count >= 3:
        print(f'Case {i+1}: Triple pangram!!!')
    elif min_count == 2:
        print(f'Case {i+1}: Double pangram!!')
    elif min_count == 1:
        print(f'Case {i+1}: Pangram!')
    else:
        print(f'Case {i+1}: Not a pangram')

        