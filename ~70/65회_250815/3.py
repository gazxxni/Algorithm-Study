# x1, y1, x2, y2 = map(int, input().split())
# x3, y3, x4, y4 = map(int, input().split())

# if x1 > x3:
#     x1, x3 = x3, x1
#     y1, y3 = y3, y1
#     x2, x4 = x4, x2
#     y2, y4 = y4, y2

# if x2 == x3:
#     if y2 == y3 or y1 == y4:
#         print("POINT")
#     elif y1 <= y3 <= y2:
#         print("LINE")
#     elif y1 <= y4 <= y2:
#         print("LINE")
#     elif y3 <= y1 <= y4:
#         print("LINE")
# elif x2 > x3:
#     if y4 < y1 or y2 < y3:
#         print("NULL")
#     elif y4 == y1 or y2 == y3:
#         print("LINE")
#     else:
#         print("FACE")
# else:
#     print("NULL")



x1, y1, x2, y2 = map(int, input().split())
x3, y3, x4, y4 = map(int, input().split())

# 좌표 정규화 (왼쪽 아래, 오른쪽 위)
x1, x2 = min(x1, x2), max(x1, x2)
y1, y2 = min(y1, y2), max(y1, y2)
x3, x4 = min(x3, x4), max(x3, x4)
y3, y4 = min(y3, y4), max(y3, y4)

# 교집합 영역 계산
ix1, iy1 = max(x1, x3), max(y1, y3)  # 교집합 왼쪽 아래
ix2, iy2 = min(x2, x4), min(y2, y4)  # 교집합 오른쪽 위

if ix1 > ix2 or iy1 > iy2:
    print("NULL")
elif ix1 == ix2 and iy1 == iy2:
    print("POINT")
elif ix1 == ix2 or iy1 == iy2:
    print("LINE")
else:
    print("FACE")
