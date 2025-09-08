import sys

n = int(input())

array = []
for _ in range(n):
    array.append(list(map(int, input().split())))

array.sort()

dp = [0] * n
dp[0] = array[0][2]

for i in range(1, n):
    # 현재 작업을 선택하지 않는 경우
    not_select = dp[i - 1]
    
    # 현재 작업을 선택하는 경우
    # 이전 작업 중 겹치지 않는 마지막 작업을 찾아서 수익을 더함
    select = array[i][2]
    if i > 1:
        select += dp[i - 2]
    
    dp[i] = max(not_select, select)

print(dp[n - 1])






"""
i = 1  /  not_select = dp[0] = 80
  /  select = array[1][2] = 60  / dp[1] = 80
i = 2  /  not_select = dp[1] = 80
  /  select = array[2][2] = 70  / dp[2] = 80
i = 3  /  not_select = dp[2] = 80
  /  select = array[3][2] + dp[0] = 100 + 80 = 180  / dp[3] = 180
i = 4  /  not_select = dp[3] = 180 
 /  select = array[4][2] + dp[2] = 40 + 80 = 120  / dp[4] = 180
i = 5  /  not_select = dp[4] = 180 
 /  select = array[5][2] + dp[3] = 50 + 180 = 230 / dp[5] = 230
"""