import sys

n, b, h, w = map(int, input().split())
min_ans = float('inf')  # 최소 비용 초기화

for _ in range(h):
    p = int(input())  
    arr = list(map(int, input().split()))  

    for i in arr:
        if i >= n:  # 숙박 가능한한 방이 있는 경우
            a = p * n  # 전체 숙박 비용 계산

            if a <= b:  # 전체 비용이 예산보다 작거나 같으면
                min_ans = min(min_ans, a)  # 최소 비용 업데이트

# 최종적으로 최소 비용이 갱신되지 않았으면 예산 초과로 숙박 불가
if min_ans == float('inf'):  
    print("stay home") 
else:
    print(min_ans) 
