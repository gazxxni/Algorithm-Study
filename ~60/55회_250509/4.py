import sys
input = sys.stdin.readline

m, n = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(m)]

def ranking(arr):
    n = len(arr)
    rank = [0] * n
    order = list(range(n))

    order.sort(key=lambda i: arr[i])

    r = 0
    for i in range(n):
        if i > 0 and arr[order[i]] != arr[order[i - 1]]:
            r = i
        rank[order[i]] = r

    a = ' '.join(map(str, rank))

    return a


def answer(arr):
    dict_a = {}

    for i in arr:
        key = ranking(i)
        if key in dict_a:
            dict_a[key] += 1
        else:
            dict_a[key] = 1

    result = 0
    for i in dict_a.values():
        if i >= 2:
            result += i * (i - 1) // 2 
            
    return result


print(answer(arr))
