import sys
input = sys.stdin.readline

n, k = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort(reverse=True)  # 큰 숫자부터 정렬 (최대값을 우선 선택하기 위해)

def find_max_number(n, arr):
    n = str(n)
    length = len(n)

    for i in range(length):
        for j in arr:
            if str(j) <= n[i]:  # 현재 자리에서 선택 가능한 가장 큰 숫자 찾기
                new_number = n[:i] + str(j)

                if j < int(n[i]):  # 현재 자리 숫자보다 작은 숫자를 골랐다면, 뒤를 최댓값으로 채우기
                    new_number += str(arr[0]) * (length - i - 1)
                    return int(new_number)
                break  # 현재 자리에서 가장 큰 값을 찾았으므로 다음 자리로 진행
        else:
            # 만약 선택 가능한 숫자가 없으면, 자리수를 줄여서 최댓값을 채운 숫자로 반환
            return int(str(arr[0]) * (length - 1))

    return int(new_number)

print(find_max_number(n, arr))





"""
정렬 부분 O(k log k)  ->  k는 최대 3이므로 O(1)
메인 반복문 n의 자리수 최대 8, arr 최대 3  ->  O(24) -> O(1)
"""
