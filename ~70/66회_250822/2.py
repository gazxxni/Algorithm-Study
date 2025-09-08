import sys
input = sys.stdin.readline

t = int(input())

for _  in range(t):
    a, b = map(int, input().split())
    arr = []
    
    while True:
        arr.append(a)
        
        if a == 1:
            break
        
        if a % 2 == 0:
            a //= 2
        else:
            a = (a - 1) // 2
            
    while True:
        if b in arr:
            print(b * 10)
            break
        
        if b % 2 == 0:
            b //= 2
        else:
            b = (b - 1) // 2
            
