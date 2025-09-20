import sys
input = sys.stdin.readline

a = int(input())
x = int(input())
MOD = 1_000_000_007

arr = [0]
brr = [1]
num = a
b = 1
for _ in range(64):
    num **= 2
    arr.append(num)
    b *= 2
    brr.append(b)

ans = 1
arr.sort(reverse=True)
brr.sort(reverse=True)

for i in range(len(brr)):
    if x - brr[i] > 0:
        x -= brr[i]

        ans *= arr[i + 1]
    
print(ans)
