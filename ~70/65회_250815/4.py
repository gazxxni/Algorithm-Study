import sys
input = sys.stdin.readline
from collections import deque

t = int(input())

for _  in range(t):
    n, m = map(int, input().split())
    graph = [[] for _ in range(n + 1)]
    visited = [0] * (n + 1)
    flag = True
    
    for _ in range(m):
        x, y = map(int, input().split())
        graph[x].append(y)
        graph[y].append(x)

        
    for i in range(1, n + 1):
        if visited[i] != 0:
            continue
        
        visited[i] = 1
        q = deque([i])

        while q:
            a = q.popleft()
            
            for n in graph[a]:
                if visited[n] == 0:
                    if visited[a] == 1:
                        visited[n] = 2
                    else:
                        visited[n] = 1
                    q.append(n)
                
                elif visited[n] == visited[a]:
                    flag = False
                    break        
        
    if flag:
        print("possible")
    else:
        print("impossible")
        