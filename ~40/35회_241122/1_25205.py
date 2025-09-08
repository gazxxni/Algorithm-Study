import sys

arr = ['q', 'w', 'e', 'r', 't', 'a', 's', 'd', 'f', 'g', 'z', 'x', 'c', 'v' ]

n = int(input())
s = list(input())


if s[-1] in arr:
    print('1')
else:
    print('0')
