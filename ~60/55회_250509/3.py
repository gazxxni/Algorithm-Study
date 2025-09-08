import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
arr = list(map(int, input().split()))

graph = [[] for _ in range(n)]
for i in range(n - 1):
    for j in range(i + 1, n):
        cost = (j - i) * (1 + abs(arr[i] - arr[j]))
        graph[i].append((j, cost)) 
        
def bfs(max_limit):
    visited = [False] * n
    q = deque([0])
    visited[0] = True

    while q:
        current = q.popleft()
        if current == n - 1:
            return True
        for neighbor, cost in graph[current]:
            if cost <= max_limit and not visited[neighbor]:
                visited[neighbor] = True
                q.append(neighbor)
    return False

left = 1
max_cost = 0

for i in range(n - 1):
    for j in range(i + 1, n):
        cost = (j - i) * (1 + abs(arr[i] - arr[j]))
        if cost > max_cost:
            max_cost = cost

right = max_cost
answer = right

while left <= right:
    mid = (left + right) // 2
    if bfs(mid):
        answer = mid
        right = mid - 1
    else:
        left = mid + 1

print(answer)
