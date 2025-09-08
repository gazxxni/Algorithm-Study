import sys

n = int(input())
arr = list(map(int, input().split()))

dp = [0] * n
ans = arr[0]

for i in range(1, n):
    ans = min(ans, arr[i])    # 현재까지의 최소값 찾기
    dp[i] = max(dp[i-1], arr[i] - ans)  # 이전 최대값과 현재 최대값 중 더 큰 값 찾기

print(*dp)   # 공백으로 구분된 형태로 출력
