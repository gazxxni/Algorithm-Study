import sys
input = sys.stdin.readline

n = int(input())
k = int(input())

def factor(x):
    d = 2 

    while d <= x:  # x가 1이 될 때까지 반복
        if d > k:  # 만약 현재 나누려는 수 d가 k보다 크다면 실패
            return 0
        
        if x % d == 0: 
            x /= d
        else:
            d += 1  # 안 나누어 떨어지면 다음 수로 증가

    return 1  # 끝까지 k 이하의 수들로 나누어졌다면 성공


ans = 0
for i in range(2, n+1):
    if factor(i):
        ans += 1

print(ans+1)






"""
while문은 d가 k까지 증가하므로 O(k)
for문은 O(n)
따라서 전체 시간 복잡도는 O(n*k)
"""