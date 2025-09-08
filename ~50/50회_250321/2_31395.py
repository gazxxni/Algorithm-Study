import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

cnt = 0
leng = 1  

for i in range(1, n):
    if arr[i - 1] < arr[i]:
        leng += 1
    else:
        cnt += leng * (leng + 1) // 2  
        leng = 1  

cnt += leng * (leng + 1) // 2

print(cnt)
