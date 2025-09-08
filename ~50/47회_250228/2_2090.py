n = int(input())
arr = list(map(int, input().split()))

def gcd(a, b):  # 유클리드 알고리즘으로 최대공약수 구하기
    while b:
        temp = a % b
        a = b
        b = temp
    return a


def solve():
    p = 1
    for a in arr:
        p *= a

    s = 0
    for a in arr:
        s += p // a

    g = gcd(p, s)

    x = p // g
    y = s // g

    print(str(x) + "/" +  str(y))

solve()