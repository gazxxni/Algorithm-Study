import sys
input = sys.stdin.readline

t = int(input())

def search(brr, x):
    st, ed = 0, len(brr) - 1
    aa = brr[0]
    
    while st <= ed:
        mid = (st + ed) // 2
        mid_a = brr[mid]
        
        if abs(mid_a - x) < abs(aa - x):
             aa = mid_a
             
        elif abs(mid_a - x) == abs(aa - x):
            aa = min(aa, mid_a)        
        
        if mid_a < x:
            st = mid + 1
            
        else:
            ed = mid - 1
            
    return aa
             

for _ in range(t):
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    brr = list(map(int, input().split()))
    crr = []

    brr.sort()
    
    for i in arr:
        crr.append(search(brr, i))
        
    print(sum(crr))
