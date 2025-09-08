import sys
input = sys.stdin.readline

while True:
    n = int(input())

    if n == 0:
        break

    arr = []

    for _ in range(n):
        a = int(input())
        arr.append(a)

    for i in range(1, len(arr)):
        arr[i] = max(arr[i] + arr[i-1], arr[i])
    

    print(max(arr))




"""
리스트 입력 → O(n)
반복문 → O(n)
최대값 찾기 → O(n)
"""