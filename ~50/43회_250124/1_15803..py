arr = [list(map(int, input().split())) for _ in range(3)]

if (arr[1][0]-arr[0][0]) * (arr[2][1]-arr[0][1]) - (arr[1][1]-arr[0][1]) * (arr[2][0]-arr[0][0]) == 0:
    print('WHERE IS MY CHICKEN?')
else:
    print('WINNER WINNER CHICKEN DINNER!')

"""
CCW 알고리즘
세 점 A(x1,y1), B(x2,y2), C(x3,y3)에 대해
(x2-x1)⋅(y3-y1)-(y2-y1)⋅(x3-x1) 의 결과값이 0이라면
A, B, C는 일직선 상에 있음음.
"""

# arr.sort()

# if arr[0][0] == arr[1][0] == arr[2][0]:
#     print("WHERE IS MY CHICKEN?")

# elif arr[0][1] == arr[1][1] == arr[2][1]:
#     print("WHERE IS MY CHICKEN?")

# elif arr[0][1]//arr[0][0] == arr[1][1]//arr[1][0] == arr[2][1]//arr[2][0]:
#     print("WHERE IS MY CHICKEN?")

# else:
#     print("WINNER WINNER CHICKEN DINNER!")


