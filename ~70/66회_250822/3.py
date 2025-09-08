import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
left = list(map(int, input().split()))
right = list(map(int, input().split()))

ans = float('inf')

aa = [0] * n
for i in range(1, n):
    aa[i] = aa[i - 1] + left[i - 1]

bb = [0] * n
for i in range(n - 2, -1, -1):
    bb[i] = bb[i + 1] + right[i]
    
idx = 0
for i in range(n):
    tmp = ans
    ans = min(ans, aa[i] + arr[i] + bb[i])
    
    if tmp != ans:
        idx = i

print(idx + 1, ans)