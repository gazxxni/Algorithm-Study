'''
순열로 다 구하면 메모리 초과
'''

# from itertools import permutations

# s = list(input().rstrip())

# arr = set(permutations(s))
# cnt = 0

# for i in arr:
#     flag = True
    
#     for j in range(len(i) - 1):
#         if i[j] == i[j + 1]:
#             flag = False
#             break
        
#     if flag:
#         cnt += 1
            
# print(cnt)


s = list(input().rstrip())
l = len(s)
dic = {}

for i in s:
    dic[i] = dic.get(i, 0) + 1

cnt = 0
def back(dic, before, use):
    global cnt
    if use == l:
        cnt += 1
        return
    
    for k, v in dic.items():
        if v > 0 and k != before:
            dic[k] -= 1
            back(dic, k, use + 1)
            dic[k] += 1

back(dic, None, 0)
print(cnt)
