n, m = map(int, input().split())
arr = input().strip()
brr = input().strip()
t = int(input())

ants = []
for i in range(n - 1, -1, -1):
    ants.append((arr[i], 'R'))

for i in range(m):
    ants.append((brr[i], 'L'))

for _ in range(t):
    i = 0
    while i < len(ants) - 1:
        if ants[i][1] == 'R' and ants[i+1][1] == 'L':
            ants[i], ants[i+1] = ants[i+1], ants[i]
            i += 2
        else:
            i += 1

result = ''
for i in range(len(ants)):
    result += ants[i][0]
print(result)
