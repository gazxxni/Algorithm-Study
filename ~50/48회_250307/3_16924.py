import sys
n, m = map(int, sys.stdin.readline().split())
arr = [list(sys.stdin.readline().strip()) for _ in range(n)] 
ans = [] 

def get_max_cross_size(x, y):
    up = down = left = right = 0 

    # 위쪽 탐색
    i = x - 1
    while i >= 0 and arr[i][y] == '*':  
        up += 1
        i -= 1  

    # 아래쪽 탐색
    i = x + 1
    while i < n and arr[i][y] == '*':  
        down += 1
        i += 1  

    # 왼쪽 탐색
    j = y - 1
    while j >= 0 and arr[x][j] == '*':  
        left += 1
        j -= 1  

    # 오른쪽 탐색
    j = y + 1
    while j < m and arr[x][j] == '*':  
        right += 1
        j += 1  

    return min(up, down, left, right) 

brr = [['.'] * m for _ in range(n)]  # 십자가를 복원할 배열 ('.'으로 채운다)

for i in range(n):
    for j in range(m):
        if arr[i][j] == "*":  # '*'이면 십자가 중심
            s = get_max_cross_size(i, j) 
            
            # 최대 크기 `s`부터 1까지 모든 크기의 십자가 추가
            for size in range(s, 0, -1):
                ans.append((i + 1, j + 1, size)) 
                brr[i][j] = '*'  # 중심에 '*' 저장

                # 십자가의 팔 부분을 복원 배열(brr)에 저장
                for k in range(1, size + 1):
                    if i - k >= 0:
                        brr[i - k][j] = '*'
                    if i + k < n:
                        brr[i + k][j] = '*'
                    if j - k >= 0:
                        brr[i][j - k] = '*'
                    if j + k < m:
                        brr[i][j + k] = '*'

# 복원한 배열(brr)과 원본 배열(arr) 비교
if brr == arr:
    print(len(ans)) 
    for i in ans:
        print(*i)
else:
    print(-1)  # 십자가만으로 원본을 만들 수 없으면 -1 출력






"""
get_max_cross_size  ->  O(N)
이중 루프  ->  O(N x M x N) = O(N²M)
2차원 리스트를 비교하는 연산  ->  O(NM)
"""