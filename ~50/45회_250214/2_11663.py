import sys
input = sys.stdin.readline 

n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()

# `min_a(a)`: a 이상(≥ a)인 첫 번째 위치 찾기
def min_a(a):  
    st, ed = 0, n 
    while st < ed:
        mid = (st + ed) // 2 
        if arr[mid] < a:  
            st = mid + 1
        else:  
            ed = mid
    return st  # a 이상이 되는 첫 번째 위치 반환

# `max_b(b)`: b 이하(≤ b)인 마지막 위치의 다음 인덱스 찾기
def max_b(b): 
    st, ed = 0, n 
    while st < ed:
        mid = (st + ed) // 2  
        if arr[mid] <= b:  
            st = mid + 1
        else:  
            ed = mid
    return st  # b 이하의 마지막 위치 + 1 반환

for _ in range(m):
    a, b = map(int, input().split()) 
    print(max_b(b) - min_a(a))  # b 이하 개수 - a 이상 개수 = 선분 내 점 개수





"""
각 이진 탐색 함수 O(log N)
M개의 쿼리 처리 → O(M log N)
정렬 O(N log N) + 탐색 O(M log N)
총 시간복잡도: O((N + M) log N)
"""