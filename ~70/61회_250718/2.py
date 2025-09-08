import sys
input = sys.stdin.readline

n = int(input())
a, b = map(int, input().split())
c = int(input())
d = [int(input()) for _ in range(n)]

d.sort(reverse=True)

ans = float(c // a)

for i in range(n):
    c += d[i]
    bbb = a + b * (i + 1)
    
    ans = max(ans, c // bbb)
    
print(int(ans))