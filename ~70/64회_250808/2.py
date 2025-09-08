import sys
input = sys.stdin.readline

n = int(input())
dic_x = {}
dic_y = {}

for _ in range(n):
    x, y = map(int, input().split())
    
    if x not in dic_x.keys():
        dic_x[x] = 1
    else:
        dic_x[x] += 1
        
    if y not in dic_y.keys():
        dic_y[y] = 1
    else:
        dic_y[y] += 1
        
cnt = 0

for _, v in dic_x.items():
    if v >= 2:
        cnt += 1
        
for _, v in dic_y.items():
    if v >= 2:
        cnt += 1
        
print(cnt)