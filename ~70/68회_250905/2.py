import sys
input = sys.stdin.readline

a, b, c = map(int, input().split())
x, y, z = map(int, input().split())

cnt = 0

for _ in range(5):
    
    if a >= x:
        cnt += x
        a -= x
        x = 0
        # print('a:', a, 'x:', x)
    else:
        cnt += a
        x -= a
        xx = x // 3
        x -= xx * 3
        y += xx
        a = 0
        # print('a:', a, 'x:', x)
        
    if b >= y:
        cnt += y
        b -= y
        y = 0
        # print('b:', b, 'y:', y)
    else:
        cnt += b
        y -= b
        yy = y // 3
        y -= yy * 3
        z += yy
        b = 0
        # print('b:', b, 'y:', y)
        
    if c >= z:
        cnt += z
        c -= z
        z = 0
        # print('c:', c, 'z:', z)
    else:
        cnt += c
        z -= c
        zz = z // 3
        z -= zz * 3
        x += zz
        c = 0
        # print('c:', c, 'z:', z)
        
print(cnt)