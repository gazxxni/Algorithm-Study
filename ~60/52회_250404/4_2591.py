a = list(input())
cnt = 0
arr = [[0] for _ in range(len(a))] 

for i in range(len(a)):
    b = int(a[i] + a[i+1])
    if b <= 34:
        arr[i].append(b)

