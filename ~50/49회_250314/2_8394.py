import sys
input = sys.stdin.readline

n = int(input())

dp = [0] * (n + 1)
dp[0] = 1
dp[1] = 1

for i in range(2, n + 1):
    dp[i] += dp[i - 1] + dp[i - 2]
    dp[i] %= 10 

print(dp[n])






"""
n 이 1일 때는 악수를 안하는 경우, 
n이 2일 때는 악수를 안하는 경우와 둘이 악수를 하는 경우.
n 이 3일 때는 세번째 사람이 악수를 안할경우, 
이 때는 두명이 있을 경우와 같기 때문에 dp[i-1] 과 같음음.
세번째 사람이 악수를 할 경우, 
첫번째 사람이 혼자 남기 때문에 dp[n-2]와 같음음.
1의 자리만 넣으라 해서 %10.
"""