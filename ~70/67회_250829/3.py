import sys
input = sys.stdin.readline

def is_primenum(n):
    prime = [True] * (n + 1)
    prime[0] = prime[1] = False
    
    for i in range (2, int(n ** 0.5) + 1):
        if prime[i]:
            for j in range(i*i, n+1, i):
                prime[j] = False
    
    primenum = []
    for i in range(2, n+1):
        if prime[i]:
            primenum.append(i)

    return primenum

def aa(n):
    arr = list(map(int, str(n)))  
    cnt = 0
    limit = 100
    
    while True:
        a = 0
        for i in arr:
            a += i ** 2
        
        if a == 1:
            return True
        
        arr = list(map(int, str(a)))
        cnt += 1
        
        if cnt > limit:
            return False
        
        
n = int(input()) 
a = is_primenum(n)

for i in a:
    if aa(i):
        print(i)
    