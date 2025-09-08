n = int(input())
arr = list(map(int, input().split()))

ans = -1
for i in range(n+1):
    cnt = arr.count(i) 
    if cnt == i:
        ans = max(ans, i)

print(ans)
    