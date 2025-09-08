n, q = map(int, input().split())
arr = [0] + list(map(int, input().split()))
brr = [list(map(int, input().split())) for _ in range(q)]

arr.sort()
a = 0
prefix_sum = [0] * (n + 1)

for i in range(1, n+1):
    a += arr[i]
    prefix_sum[i] = a

for l, r in brr:
    print(prefix_sum[r] - prefix_sum[l-1])

"""
각 질문마다 반복문을 매번 돌려서 답을 계산하면, 시간복잡도가 O(QN)이 되므로 시간 초과를 받게됨
따라서 누적합을 사용해 처리
누적 합 배열 생성은 O(n).
각 쿼리 처리도 O(1).
전체 시간 복잡도는 O(n + q).
"""


# for l, r in brr:
#     a = 0
#     for i in range(l, r+1):
#         a += i
#     print(a) 