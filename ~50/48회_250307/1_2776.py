import sys
input = sys.stdin.readline

t = int(input())

# for _ in range(t):

#     n = int(input())
#     arr = sorted(list(map(int, input().split())))
#     m = int(input())
#     brr = list(map(int, input().split()))
    
#     for i in brr:
#         st, ed = 0, n-1

#         while True:
#             mid = (st + ed) // 2

#             if arr[mid] == i:
#                 print(1)
#                 break

#             if st >= ed:
#                 print(0)
#                 break

#             if arr[mid] < i:
#                 st = mid + 1
#             else:
#                 ed = mid - 1

for _ in range(t):
    n = int(input())
    arr = set(map(int, input().split()))
    m = int(input())
    brr = list(map(int, input().split()))

    for i in brr:
        if i in arr:
            print(1)
        else:
            print(0)