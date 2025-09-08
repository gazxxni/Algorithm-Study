import sys
input = sys.stdin.readline

m = int(input())
sum = 0 
xor = 0

for i in range(m):
    arr = list(map(int, input().split()))

    if arr[0] == 1:
        sum += arr[1]
        xor ^= arr[1]

    elif arr[0] == 2:
        sum -= arr[1]
        xor ^= arr[1]

    elif arr[0] == 3:
        print(sum)

    else:
        print(xor)





"""
A ^ A = 0  (같은 숫자를 XOR 하면 0)
A ^ 0 = A  (0과 XOR 하면 A 그대로 유지)
xor = 0
-----------------------------------------
xor ^= 4  # xor = 0 ^ 4 = 4
xor ^= 7  # xor = 4 ^ 7 = 3
xor ^= 4  # xor = 3 ^ 4 = 7 (4 제거)
print(xor)  # 7
-----------------------------------------
반복문 O(m)
"""