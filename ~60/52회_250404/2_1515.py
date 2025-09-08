import sys
input = sys.stdin.readline

a = input().rstrip() 
    
idx = 0  # 배열의 위치를 가리킬 포인터
length = len(a)
    
num = 1
while idx < length:
    s = str(num)

    print('숫자  : ', s, ' 인덱스: ', idx,)
    # 해당 숫자의 각 자리를 배열과과 순서대로 매칭 시도
    for i in s:
        print('현재 i: ', i, ' a[idx]: ', a[idx])
        if i == a[idx]:
            idx += 1
            if idx == length:
                break
    num += 1
    
# idx == length 순간의 num은 이미 1 증가한 상태이기에 -1
print(num - 1)