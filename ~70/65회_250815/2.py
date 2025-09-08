import sys
input = sys.stdin.readline

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
arr.sort()
    
def search():
    dp = [0] * (n + 1)
    dp[0] = arr[0][2]
    dp[1] = arr[0][2]

    for i in range(2, n):
        dp[i] = max(dp[i-1], dp[i-2] + arr[i][2])
        
    a = dp[n-1]

    dp = [0] * (n + 1)
    dp[0] = arr[0][2]
    dp[1] = arr[1][2]

    for i in range(2, n):
        dp[i] = max(dp[i-1], dp[i-2] + arr[i][2])

    b = dp[n-1]

    print(max(a, b))
    
if n == 1:
    print(arr[0][2])
else:
    search()
