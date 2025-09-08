import sys
input = sys.stdin.readline

n = int(input())
arr = []
max = 0
ans = 0

for i in range(n):
    a = list(map(int, input().split()))

    if a[0] == 1:
        arr.append(a[1])
    else:
        arr.pop(0)

    if max < len(arr):
        max = len(arr)
        ans = arr[-1]

    elif max == len(arr):
        ans = min(ans, arr[-1])

print(max, ans)


