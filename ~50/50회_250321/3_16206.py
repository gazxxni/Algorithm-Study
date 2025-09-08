import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().split()))

cnt = 0
brr = []

for x in arr:
    if x == 10:
        cnt += 1
    elif x > 10:
        brr.append(x)

brr.sort(key=lambda x: (x % 10 != 0, x))


for x in brr:
    if x < 10:
        continue

    if x % 10 == 0:
        a = x // 10 - 1
        if m >= a:
            cnt += x // 10
            m -= a
        else:
            cnt += m
            m = 0
    else:
        a = x // 10
        if m >= a:
            cnt += a
            m -= a
        else:
            cnt += m
            m = 0

    if m == 0:
        break

print(cnt)
