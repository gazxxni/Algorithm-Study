import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
x, y = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(m)]

graph = [[-1] * n for _ in range(n)]

directions = [(-2, -1), (-2, 1), (2, -1), (2, 1),
              (-1, -2), (-1, 2), (1, -2), (1, 2)]

def bfs(x, y):
    q = deque()
    q.append((x, y))
    graph[x][y] = 0

    while q:
        cx, cy = q.popleft()
        for dx, dy in directions:
            nx, ny = cx + dx, cy + dy
            if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] == -1:
                graph[nx][ny] = graph[cx][cy] + 1
                q.append((nx, ny))

bfs(x-1, y-1)

for x, y in arr:
    print(graph[x-1][y-1], end=' ')
