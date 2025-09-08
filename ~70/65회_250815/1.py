t = int(input())

for _ in range(t):
    n = int(input())
    num = n
    cnt = 0
    
    while True:
        if num == 6174:
            print(cnt)
            break
        
        a = (num // 1000) % 10
        b = (num // 100) % 10
        c = (num // 10) % 10
        d = num % 10
        
        a, b, c, d = sorted([a, b, c, d])
        min_v = 1000 * a + 100 * b + 10 * c + d   
             
        a, b, c, d = sorted([a, b, c, d], reverse=True)
        max_v = 1000 * a + 100 * b + 10 * c + d
        
        num = max_v - min_v
        cnt += 1