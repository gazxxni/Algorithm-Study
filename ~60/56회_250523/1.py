import sys
input = sys.stdin.readline

n = int(input())

arr = set()
cnt = 0

for _ in range(n):
    a, b = map(int, input().split())

    if b == 1:
        if a in arr:
            cnt += 1
        else:
            arr.add(a)
    elif b == 0:
        if a in arr:
            arr.remove(a)
        else:
            cnt += 1

print(len(arr) + cnt)
