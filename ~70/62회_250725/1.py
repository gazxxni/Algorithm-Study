import sys, math
input = sys.stdin.readline

n = int(input())
arr = list(input().rstrip())

c = arr.count('C')
if c == 0:
    print(0)
elif n == c:
    print(n)
else:
    other = n - c + 1
    print(math.ceil(c / other))