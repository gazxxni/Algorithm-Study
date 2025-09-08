h, w = map(int, input().split())
graph = [input().strip() for _ in range(h)]

ans = 0

for i in graph:
    inside = False
    cnt = 0.0 
    
    for j in i:
        if j == '/' or j == '\\':
            inside = not inside 
            cnt += 0.5 
        elif inside:
            cnt += 1 
    
    ans += cnt

print(int(ans))  