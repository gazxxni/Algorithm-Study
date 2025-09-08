import sys
input = sys.stdin.readline

n = int(input())
a = input().rstrip()
b = input().rstrip()

if a[0] != b[0] or a[-1] != b[-1]:
    print("NO")

else:
    alphabet = {
        'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0,
        'h': 0, 'i': 0, 'j': 0, 'k': 0, 'l': 0, 'm': 0, 'n': 0,
        'o': 0, 'p': 0, 'q': 0, 'r': 0, 's': 0, 't': 0, 'u': 0,
        'v': 0, 'w': 0, 'x': 0, 'y': 0, 'z': 0
    }

    for i in a:
        alphabet[i] += 1

    for j in b:
        alphabet[j] -= 1

    for k in alphabet.values():
        if k != 0:
            print("NO")
            break

    else:
        aeiou = {'a', 'e', 'i', 'o', 'u'}

        arr = []
        for i in a:
            if i not in aeiou:
                arr.append(i)

        brr = []
        for j in b:
            if j not in aeiou:
                brr.append(j)

        if arr == brr:
            print("YES")
        else:
            print("NO")