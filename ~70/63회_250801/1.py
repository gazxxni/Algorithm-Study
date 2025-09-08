t = int(input())

for _ in range(t):
    n, m, k, d = map(int, input().split())
    a = 0
    b = 1
    cc = 9999999999
    
    while True:
        a = k * b
        
        same = m * (m - 1) // 2 * a * n
        other = n * (n - 1) // 2 * m * m * b

        if b == 1 and same + other > d:
            print(-1)
            break
        
        if same + other < d:
            cc = min(cc, abs(same + other - d))
            tmp_a = same
            tmp_b = other
            b += 1
        
        elif same + other == d:
            print(d)
            break
        
        else:
            print(tmp_a + tmp_b)
            break
        