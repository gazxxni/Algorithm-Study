import sys
input = sys.stdin.readline
from collections import deque

n, m = map(int, input().split())
a, b, c = map(int, input().split())
arr = [[] * (n + 1) for _ in range(m + 1)]
for _ in range(m):
    i, j, k = map(int, input().split())
    arr[i].append((j, k))
    arr[j].append((i, k))

def bfs(start, node):
    visited = set()
    q = deque()
    q.append(start)
    visited.add(start)
    
    while q:
        x = q.popleft()
        
        