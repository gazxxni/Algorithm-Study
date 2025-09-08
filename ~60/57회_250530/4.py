import sys
from collections import deque
input = sys.stdin.readline

n, k = map(int, input().split())
visited = [False] * (n + 100000)
limit = len(visited)

def bfs(n, k):

    queue = deque()
    queue.append((0, 0)) 

    while queue:
        now, cnt = queue.popleft()

        if cnt > k:
            continue

        if now == n and cnt == k:
            return True 

        if now + 1 < limit and not visited[now + 1]:
            visited[now + 1] = True
            queue.append((now + 1, cnt + 1))

        next_pos = now + now // 2
        if next_pos < limit and not visited[next_pos]:
            visited[next_pos] = True
            queue.append((next_pos, cnt + 1))

    return False  

a = bfs(n, k)

if a:
    print("minigimbob")
else:
    print("water")
