n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

directions = [
    [(0, 0), (1, 0), (0, 1)],  
    [(0, 0), (1, 0), (0, -1)],
    [(0, 0), (-1, 0), (0, 1)],  
    [(0, 0), (-1, 0), (0, -1)]  
]

visited = [[False] * m for _ in range(n)]
ans = 0

def back(x, y, cnt):
    global ans
    
    if y == m:
        x += 1
        y = 0
        
    if x == n:
        ans = max(ans, cnt)
        return
    
    if not visited[x][y]:
        for i in directions:
            tmp = 0
            
            for dx, dy in i:
                nx, ny = x + dx, y + dy
                if not (0 <= nx < n and 0 <= ny < m) or visited[nx][ny]:
                    break
                if dx == 0 and dy == 0:
                    tmp += arr[nx][ny] * 2
                else:
                    tmp += arr[nx][ny]
                    
            else:  
                for dx, dy in i:
                    nx, ny = x + dx, y + dy
                    visited[nx][ny] = True
                    
                back(x, y+1, cnt + tmp) 
                
                for dx, dy in i:
                    nx, ny = x + dx, y + dy
                    visited[nx][ny] = False
                    
    back(x, y+1, cnt)                
                    
back(0, 0, 0)
print(ans)