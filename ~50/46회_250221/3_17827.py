import sys
input = sys.stdin.readline

n, m, v = map(int, input().split())
arr = list(map(int, input().split()))
brr = []

for i in range(v-1, n):
    brr.append(arr[i])

for _ in range(m):
    k = int(input())
    if k < n:
        print(arr[k])
    else:
        print(brr[(k-n) % (n-v+1)])  # brr의 길이 = n-v+1
        # k-n 반복 구간에서의 상대적 위치를 찾을 수 있음




"""
입력 → O(n)
v 이후의 값만 저장 → O(n)
질의 처리 반복복 → O(m)
"""