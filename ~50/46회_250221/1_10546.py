import sys
input = sys.stdin.readline

n = int(input())
arr = dict()

for _ in range(n):
    name = input().strip()
    if name not in arr.keys(): # 선수가 처음 등장하면면
        arr[name] = 1  # 1로 하고
    else:
        arr[name] += 1  # 동명이인이면 1 증가

for _ in range(n-1):
    name = input().strip()
    if name in arr.keys():  # 완주한 선수는 1 감소
        arr[name] -= 1

for key, value in arr.items():
    if value % 2 == 1:  # 완주하지 못한 선수는 1이 남음
        print(key)
        break



"""
출전 선수 입력 → O(n)
완주 선수 입력 → O(n)
미완주자 찾기 → O(n)
"""