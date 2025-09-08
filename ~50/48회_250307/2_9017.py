for _ in range(int(input())):

    n = int(input())
    arr = list(map(int, input().split()))
    cnt_dict = {}

    for i in range(n):
        if arr[i] in cnt_dict:
            cnt_dict[arr[i]] += 1
        else:
            cnt_dict[arr[i]] = 1

    select_dict = {}
    for k, v in cnt_dict.items():
        if v >= 6:
            select_dict[k] = []

    score = 1
    for k in arr:
        if k in select_dict:
            select_dict[k].append(score)
            score += 1

    win = None
    best_total = float('inf')
    best_ = float('inf')
    for k, v in select_dict.items():
        total = sum(v[:4])
        fifth = v[4]
        if total < best_total or (total == best_total and fifth < best_fifth):
            best_total = total
            best_fifth = fifth
            win = k

    print(win)