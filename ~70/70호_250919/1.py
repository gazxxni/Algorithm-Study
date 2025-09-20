t = int(input())

arr = [''] * 5
arr[1] = 'VV'
arr[2] = 'V딸기'
arr[3] = '딸기V'
arr[4] = '딸기딸기'

for _ in range(t):
    n = int(input())
    
    a = n % 28
    ans = []
    if 1 <= a <= 3 or a == 27:
        if a > 3:
            a = 30 - a
        ans.append(arr[1] + arr[a + 1]) 
    
    elif 4 <= a <= 7 or 23 <= a <= 26:
        if a > 7:
            a = 30 - a
        ans.append(arr[2] + arr[a - 3])   
            
    elif 8 <= a <= 11 or 19 <= a <= 22:
        if a > 11:
            a = 30 - a
        ans.append(arr[3] + arr[a - 7])
    
    elif 12 <= a <= 18:
        if a > 15:
            a = 30 - a
        ans.append(arr[4] + arr[a - 11])
        
    elif a == 0:
        ans.append('VV딸기V')
        

    print(*ans)