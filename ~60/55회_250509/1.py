# import sys
# input = sys.stdin.readline

# n, m = map(int, input().split())
# stack = []
# cnt = 1

# for i in range(m):
#     k = int(input())
#     arr = list(map(int, input().split()))
#     stack.append(arr)

# # print(stack)

# for _ in range(2):
#     for i in range(m):
#         if stack[i][-1] == cnt:
#             cnt += 1
#             stack[i].pop(-1)

#             if cnt == n:
#                 print("YES")
#                 break
            
#         else:
#             print("NO")


import sys
input = sys.stdin.readline

n, m = map(int, input().split())
ans = 0
for _ in range(m):
    k = int(input())
    arr = list(map(int, input().split()))
    brr = arr.copy()
    arr.sort(reverse=True)

    if arr == brr:
        ans += 1
    

if ans == m:
    print("Yes")
else:
    print("No")
    