import sys
input = sys.stdin.readline

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

t = int(input())

for _ in range(t):
    arr = list(input().rstrip())
    brr = []

    if '(' in arr:
        st = arr.index('(')
        ed = arr.index(')')
        repeat = ''.join(arr[st+1:ed])  # 반복되는 부분
        repeat_len = ed - st - 1
        
        if st > 2:
            n_repeat = ''.join(arr[2:st])
        else:
            n_repeat = ''

        if n_repeat == '':  # ex: 0.(3)
            n = int(repeat)
            nine = int('9' * repeat_len)
            
        else:    # ex: 0.12(34)
            n = int(n_repeat + repeat) - int(n_repeat)
            nine = int('9' * repeat_len + '0' * len(n_repeat))

        g = gcd(n, nine)
        aa = n // g
        bb = nine // g
        
        print(str(aa) + '/' + str(bb))


    else:   # ex: 0.123
       
        n = int(''.join(arr[2:]))
        ten = 10 ** (len(arr) - 2)

        g = gcd(n, ten)
        aa = n // g
        bb = ten // g
        print(str(aa) + '/' + str(bb))