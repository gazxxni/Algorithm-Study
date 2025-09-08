# # 모든 가능한 3x3 매직 스퀘어
graph = [
    [8, 1, 6, 3, 5, 7, 4, 9, 2],
    [6, 1, 8, 7, 5, 3, 2, 9, 4],
    [4, 9, 2, 3, 5, 7, 8, 1, 6],
    [2, 9, 4, 7, 5, 3, 6, 1, 8],
    [8, 3, 4, 1, 5, 9, 6, 7, 2],
    [4, 3, 8, 9, 5, 1, 2, 7, 6],
    [6, 7, 2, 1, 5, 9, 8, 3, 4],
    [2, 7, 6, 9, 5, 1, 4, 3, 8],
]

arr = [list(map(int, input().split())) for _ in range(3)]

brr = []
# 입력된 3x3 행렬을 1차원 배열로 변환
for row in arr:
    for num in row:
        brr.append(num)

min_cost = float('inf')

for crr in graph:
    cost = 0

    for i in range(9):
        cost += abs(brr[i] - crr[i])

    if cost < min_cost:
        min_cost = cost

print(min_cost)