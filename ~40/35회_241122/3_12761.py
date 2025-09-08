from collections import deque

def bfs(x):
    dy = [1, -1, a, -a, b, -b, a, b]
    queue = deque([x])
    visited[x] = True

    while queue:
        target = queue.popleft()

        for i in range(8):
            if i < 6:
                y = target + dy[i]
            else:
                y = target * dy[i]

            if 0 <= y <= 100000 and visited[y] == False:
                queue.append(y)
                visited[y] = True
                graph[y] = graph[target] + 1
                
                if y == m: 
                    return 


a, b, n, m = map(int, input().split())
graph = [0 for _ in range(100001)]
visited = [False for _ in range(100001)]

bfs(n)

print(graph[m])