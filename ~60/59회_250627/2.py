import sys
input = sys.stdin.readline
from collections import Counter

n = int(input())

for _ in range(n):
    arr = list(map(int, input().split()))
    t = arr[0]
    arr = arr[1:]
    arr.sort()
    aa = Counter(arr)
    
    if aa.most_common(1)[0][1] > t // 2:
        print(aa.most_common(1)[0][0])

    else:
        print("SYJKGW")