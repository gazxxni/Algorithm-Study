import sys
input = sys.stdin.readline

t = int(input())

for i in range(1, t + 1):
    n = int(input())
    arr = list(map(int, input().split()))
    visited = [False] * (2 * n)
    ans = []
    
    for j in range(2 * n):
        if visited[j]:
            continue
        a = arr[j] * 4 // 3
        
        for k in range(j + 1, 2 * n):
            if not visited[k] and arr[k] == a:
                visited[j] = visited[k] = True
                ans.append(arr[j])
                break
    
    print(f"Case #{i}:", *ans)
