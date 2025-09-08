n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
dict_a = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0}

for grade in range(1, 6):
    cnt = 0
    for li in arr:
        if grade in li:
            cnt += 1
        else:
            dict_a[grade] = max(dict_a[grade], cnt)
            cnt = 0
    dict_a[grade] = max(dict_a[grade], cnt)

sorted_items = sorted(dict_a.items(), key=lambda x: (-x[1], x[0]))
print( sorted_items[0][1], sorted_items[0][0])