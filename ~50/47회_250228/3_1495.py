n, s, m = map(int, input().split())
v = list(map(int, input().split()))

dp = [[0] * (m + 1) for _ in range(n + 1)]
dp[0][s] = 1

for i in range(n):
    for j in range(m + 1):
        if dp[i][j] == 1:  # 현재 i곡의 볼륨이 담겨있으면

            if j + v[i] <= m:  
                dp[i + 1][j + v[i]] = 1

            if j - v[i] >= 0:
                dp[i + 1][j - v[i]] = 1

ans = -1

for i in range(m, -1, -1):  # 큰 볼륨부터 탐색
    if dp[n][i] == 1:
        ans = i
        break

print(ans)
