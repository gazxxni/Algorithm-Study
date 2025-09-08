import math

a, b, d = map(int, input().split())

def primenumber(n):
    arr = [True] * (n + 1)
    arr[0] = False
    arr[1] = False

    for i in range(2, int(math.sqrt(n)) + 1):
        if arr[i] == True:
            for j in range(i * i, n + 1, i):
                arr[j] = False

    return arr

arr = primenumber(4000000)

cnt = 0
for i in range(a, b + 1):
    if arr[i] and str(d) in str(i):
        cnt += 1

print(cnt)
