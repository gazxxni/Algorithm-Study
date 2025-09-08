import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

sum_arr = sum(arr)
a = 0

for i in arr:
    a += i ** 2

ans = sum_arr ** 2 - a
print(int(ans/2))
