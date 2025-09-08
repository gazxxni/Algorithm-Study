from itertools import combinations

n = int(input())

result = []
for i in range(1, 11):  # 1자리부터 10자리까지 0, ... , 9876543210
    for j in combinations(range(10), i):  # 0부터 i까지 조합 j 생성
        num = ''.join(map(str, reversed(j)))  # 각 배열을 내림차순으로 변환 후 결합하여 문자열 반환
        result.append(int(num))

result.sort()  # [0, 1, 2, ... , 10, 20, 30, ... , 21, 31, ...] 형태로 저장되기 때문에 정렬

if n >= len(result):
    print(-1)
else:
    print(result[n])