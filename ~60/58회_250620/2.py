from collections import deque

N, M = map(int, input().split()) 
arr = [list(map(int, input().split())) for _ in range(M)]

directions = [(0, 1), (1, 0)]
visited = [[False] * N for _ in range(M)]

def bfs():
    q = deque()
    q.append((0, 0))
    visited[0][0] = True

    while q:
        x, y = q.popleft()

        if x == M - 1 and y == N - 1:
            return "Yes"

        for dx, dy in directions:
            nx = x + dx
            ny = y + dy

            if 0 <= nx < M and 0 <= ny < N:
                if not visited[nx][ny] and arr[nx][ny] == 1:
                    visited[nx][ny] = True
                    q.append((nx, ny))

    return "No"

print(bfs())
