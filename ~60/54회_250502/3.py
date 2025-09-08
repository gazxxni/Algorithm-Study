import sys
input = sys.stdin.readline
from collections import deque

n, k = map(int, input().split())
arr = list(map(int, input().split()))
visited = [False] * (n + 1)

def bfs():
    q = deque()
    q.append(0)
    visited[0] = True
    
    while q:
        aa = q.popleft()
        
        if aa == n -1:
            return "YES"
        
        for i in range(aa + 1, n):
            bb = (i - aa) * (1 + abs(arr[aa] - arr[i]))
            
            if bb <= k and not visited[i]:
                visited[i] = True
                q.append(i)
                
    return "NO"

print(bfs())