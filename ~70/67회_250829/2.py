import sys
input = sys.stdin.readline

n = int(input())
dp = [0] * 4
dp[0] = 0
dp[1] = 0
dp[2] = 1
dp[3] = 3
# dp[4] = 6
# dp[5] = 10
a = 0
b = 3
for i in range(4, n + 1):
    a = b + (i - 1)
    b = a

if n < 4:
    print(dp[n])
    
else:
    print(a)