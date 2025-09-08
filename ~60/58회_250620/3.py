import sys
input = sys.stdin.readline

n = int(input())
t = 8

cnt = 1

while True:
    if cnt < n:
        cnt *= 2
        t += 1
        
    elif cnt == n:
        print(t + 2)
        exit()
        
    else:
        print(t + 1)
        exit()