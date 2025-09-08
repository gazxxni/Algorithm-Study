import sys

n = int(input())
v = list(map(int, input().split()))

a = 0
ans = 0

for i in v[::-1]:

    if a < i:
        a += 1
    else:
        a = i
    
    ans += a

print(ans)