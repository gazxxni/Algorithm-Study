import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
brr = list(map(int, input().split()))
dic = {}
cnt = 0

for i in arr:
    if i in dic:
        dic[i] += 1
    else:
        dic[i] = 1
    
for i in brr:
    if i in dic:
        if dic[i] > 0:
            dic[i] -= 1
        else:
            cnt += 1
            
    else:
        cnt += 1
            
print(cnt)