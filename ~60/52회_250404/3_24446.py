import sys
from collections import deque
input = sys.stdin.readline

n, m, r = map(int, input().split())
arr = [[] for _ in range(n)] 

for _ in range(m):
    u, v = map(int, input().split())
    arr[u - 1].append(v - 1)
    arr[v - 1].append(u - 1)

def bfs(s):
    depth = [-1] * n
    q = deque([s])
    depth[s] = 0
    while q:
        node = q.popleft()
        for i in arr[node]:
            if depth[i] == -1:
                depth[i] = depth[node] + 1
                q.append(i)

    return depth

a = bfs(r-1)
for i in a:
    print(i)