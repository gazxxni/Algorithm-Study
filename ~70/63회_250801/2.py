n = float(input())
arr = [list(map(float, input().split())) for _ in range(3)]

a1, b1 = arr[0]
start = (a1 + b1) / 2
left = start
right = n - start

if left <= right:
    
    for i in range(1, 3):
        for j in range(2):
            if arr[i][j] < start:
                arr[i][j] = 2 * start - arr[i][j]

    for i in range(1, 3):
        for j in range(2):
            arr[i][j] -= start
    length = right
    
else:

    for i in range(1, 3):
        for j in range(2):
            if arr[i][j] > start:
                arr[i][j] = 2 * start - arr[i][j]
    length = left


a2, b2 = arr[1]

if a2 != b2:
    start = (a2 + b2) / 2
    left = start
    right = length - start

    if left <= right:
        
        for j in range(2):
            if arr[2][j] < start:
                arr[2][j] = 2 * start - arr[2][j]

        for j in range(2):
            arr[2][j] -= start
        length = right
        
    else:

        for j in range(2):
            if arr[2][j] > start:
                arr[2][j] = 2 * start - arr[2][j]
        length = left


a3, b3 = arr[2]

if a3 != b3:
    start = (a3 + b3) / 2
    left = start
    right = length - start

    length = max(left, right)

print(format(length, ".1f"))
