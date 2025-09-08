a = int(input())
arr = list(map(int, input().split()))

def jun():
    left_mon = a
    stock = 0   

    for i in arr:

        stock += left_mon // i
        left_mon = left_mon % i 

        if left_mon == 0:
            break  # 돈이 다 떨어지면 더 이상 매수 불가

    return left_mon, stock 

def sung():
    left_mon = a  
    stock = 0    

    # i, i+1, i+2, i+3 네 날을 비교하기 위해 0부터 len(arr)-4까지 순회
    for i in range(len(arr) - 4):
        # 3일 연속 상승 → 전량 매도
        if arr[i] < arr[i + 1] < arr[i + 2] < arr[i + 3]:
            left_mon += stock * arr[i + 3]
            stock = 0

        # 3일 연속 하락 → 전액 매수
        if arr[i] > arr[i + 1] > arr[i + 2] > arr[i + 3]:
            stock += left_mon // arr[i + 3]
            left_mon = left_mon % arr[i + 3]

    return left_mon, stock 


jun_m, jun_s = jun()
total_jun = jun_m + jun_s * arr[-1] 
sung_m, sung_s = sung()
total_sung = sung_m + sung_s * arr[-1] 


if total_jun < total_sung:
    print('TIMING') 
elif total_jun > total_sung:
    print('BNP')    
else:
    print('SAMESAME') 
