import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

check = [arr[i] <= arr[i+1] for i in range(n - 1)]

if all(check):
    print(n)
    exit()

if check.count(False) >= 2:
    print(0)
    exit()

idx = check.index(False)
cnt = 0

if idx == 0 or arr[idx - 1] <= arr[idx + 1]:
    if all(check[:idx]) and all(check[idx + 1:]):
        cnt += 1

if idx + 2 == n or arr[idx] <= arr[idx + 2]:
    if all(check[:idx]) and all(check[idx + 2:]):
        cnt += 1

print(cnt)