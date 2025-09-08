import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    
    arr.sort()

    cnt = 0

    for i in range(n-2):
        for j in range(i+2, n):
            mid = (arr[i] + arr[j]) / 2
            if mid == int(mid):
                if int(mid) in arr[i+1:j]:
                    cnt += 1
            
    
    print(cnt)
                 