import sys
input = sys.stdin.readline

n = int(input())
arr = []
cnt = 0

for _ in range(n):
    arr.append(int(input()))

for i in range(n-1, -1, -1):
    if arr[i] == n: # 현재 숫자가 n과 같으면 정렬된 상태
        n -= 1
    else:
        cnt += 1

print(cnt)



"""
예제 1 (3, 2, 1)
arr[3] (2) != n (4) → cnt += 1 // 결과: cnt = 1, n = 4
arr[2] (4) == n (4) → n -= 1 // 결과: cnt = 1, n = 3
arr[1] (3) == n (3) → n -= 1 // 결과: cnt = 1, n = 2
arr[0] (1) != n (2) → cnt += 1 // 결과: cnt = 2, n = 2
"""