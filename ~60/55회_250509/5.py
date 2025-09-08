import sys
from collections import deque

input = sys.stdin.readline
n = int(input())
grid = [list(input().rstrip()) for _ in range(n)]
doors = [(i, j) for i in range(n) for j in range(n) if grid[i][j] == '#']
(sy, sx), (ey, ex) = doors
dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]
inf = float('inf')
dist = [[[inf] * 4 for _ in range(n)] for _ in range(n)]

def bfs():
    dq = deque()
    for d in range(4):
        dist[sy][sx][d] = 0
        dq.append((sy, sx, d))
    while dq:
        y, x, d = dq.popleft()
        c = dist[y][x][d]
        for nd, (dy, dx) in enumerate(dirs):
            ny, nx = y + dy, x + dx
            if not (0 <= ny < n and 0 <= nx < n): 
                continue
            if grid[ny][nx] == '*':
                continue

            if nd == d:
                nc = c
            else:
                if grid[y][x] != '!':
                    continue
                nc = c + 1

            if nc < dist[ny][nx][nd]:
                dist[ny][nx][nd] = nc
                if nd == d:
                    dq.appendleft((ny, nx, nd))
                else:
                    dq.append((ny, nx, nd))
                    
    return min(dist[ey][ex])

print(bfs())
