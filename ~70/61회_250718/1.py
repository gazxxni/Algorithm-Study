n = int(input())
arr = [list(input().rstrip()) for _ in range(n)]
brr = [list(input().rstrip()) for _ in range(n)]

directions = [(0,1), (1, 0), (0, -1), (-1, 0), (1, 1), (1, - 1), (-1, 1), (-1, -1)]
flag = False

def search(cx, cy):
    cnt = 0
    
    for xx, yy in directions:
        nx = xx + cx
        ny = yy + cy
        
        if 0 <= nx < n and 0 <= ny < n and arr[nx][ny] == '*':
            cnt +=1 
            
    brr[cx][cy] = str(cnt)
        
for i in range(n):
    for j in range(n):
        if brr[i][j] == 'x':
            if arr[i][j] == '*':
                flag = True
            else:
                search(i, j)

if flag:
    for i in range(n):
        for j in range(n):
            if arr[i][j] == '*':
                brr[i][j] = '*'

        

for row in brr:
    print(*row, sep='')