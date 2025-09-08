n, k = map(int, input().split())
arr = list(map(int, input().split()))
s = sum(arr[:k])

res = s
for i in range(k, n + k):
  ni = i % n
  s += arr[ni]  # 오른쪽 값 추가
  s -= arr[ni - k]  # 왼쪽 값 감소
  res = max(res, s)  # 정답 갱신

print(res)




"""
s = sum(arr[:k])는 k개의 요소를 더하므로 O(k)
for i in range(k, n + k)는 n번 반복하므로 O(n)
총 시간 복잡도는 O(k + n) = O(n)
"""