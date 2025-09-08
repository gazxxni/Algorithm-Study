import sys
from collections import deque

n = int(input())
arr = [list(input()) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(arr):
    n = len(arr)
    q = deque([0, 0, 0, 0, 0, 0])
    visited = set()
    visited.add((0, 0, 0, 0, 0, 0))

    while q:
        x, y, j, c, b, w, s = q.popleft()

        if (x, y) == (n - 1, n - 1) and all(cnt >= 3 for cnt in (j, c, b, w)):
            return s
        
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if 0 <= nx < n and 0 <= ny < n:
                j_cnt = j
                c_cnt = c
                b_cnt = b
                w_cnt = w

                if arr[nx][ny] == 'j':
                    j_cnt += 1
                elif arr[nx][ny] == 'c':
                    c_cnt += 1
                elif arr[nx][ny] == 'b':
                    b_cnt += 1
                elif arr[nx][ny] == 'w':
                    w_cnt += 1

                state = (nx, ny, j_cnt, c_cnt, b_cnt, w_cnt)
                if state not in visited:
                    visited.add(state)
                    q.append((nx, ny, j_cnt, c_cnt, b_cnt, w_cnt))
    return -1

result = bfs(arr)

