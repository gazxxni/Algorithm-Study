import sys

input = sys.stdin.readline

n = int(input())
arr = []

for _ in range(n):
    arr.append(int(input()))

arr.sort(reverse=True)  # 내림차순 정렬

for i in range(n - 2): 
    if arr[i] < arr[i+1] + arr[i+2]:   # 삼각형 조건
        print(arr[i] + arr[i+1] + arr[i+2])  
        break
else:
    print(-1) 
