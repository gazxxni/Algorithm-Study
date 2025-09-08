t = int(input())

for _ in range(t):
    n = int(input())
    arr = [int(input()) for _ in range(n)]
    max_arr = max(arr)
    sum_arr = sum(arr)
    
    a = sum_arr // 2
    
    if arr.count(max_arr) >= 2:
        print('no winner')
        
    elif max_arr > a:
        print('majority winner', arr.index(max_arr) + 1)
    
    else:        
        print('minority winner', arr.index(max_arr) + 1)