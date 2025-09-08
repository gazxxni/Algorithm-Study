import sys
input = sys.stdin.readline

n, k = map(int, input().split())
arr = []

for _ in range(n):
    x = int(input())
    arr.append(x)

st, ed = min(arr), max(arr) + k
ans = 0

while st <= ed:
    mid = (st + ed) // 2
    cnt = 0
    
    for i in arr:
        if i < mid:
            cnt += mid - i

    if cnt <= k:
        st = mid + 1
        ans = max(ans, mid)

    else:
        ed = mid - 1

print(ans)