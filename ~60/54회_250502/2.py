import sys
from collections import deque

input = sys.stdin.readline

n, m, r = map(int, input().split())
arr = [[] for _ in range(n + 1)]
for _ in range(m):
    u, v = map(int, input().split())
    arr[u].append(v)
    arr[v].append(u)

def bfs(arr, start):

    n = len(arr) - 1
    depth = [-1] * (n + 1)
    check = [0] * (n + 1)

    q = deque([start])
    depth[start] = 0
    check[start] = 1
    cnt = 1

    while q:
        u = q.popleft()
        for v in arr[u]:
            if depth[v] == -1:
                q.append(v)
                depth[v] = depth[u] + 1
                cnt += 1
                check[v] = cnt

    return depth, check

for lst in arr:
    lst.sort()

depth, check = bfs(arr, r)

result = 0
for i in range(1, n + 1):
    result += depth[i] * check[i]

print(result)
