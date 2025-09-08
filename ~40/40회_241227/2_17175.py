import sys
n = int(input())

dp = [0] * 51  
dp[0] = 1  # F(0) 호출 횟수는 1 
dp[1] = 1  # F(1) 호출 횟수는 1 

for i in range(2, n + 1):
    # F(i) 호출 횟수 = F(i-1) 호출 횟수 + F(i-2) 호출 횟수 + 1
    # (현재 F(i)를 직접 호출하는 횟수 1을 포함)
    dp[i] = (dp[i - 1] + dp[i - 2] + 1) % 1000000007  

print(dp[n])

