import sys
input = sys.stdin.readline

m, s = map(int, input().strip().split(':'))
total = m * 60 + s

if total == 30:
    print(1)
    exit()

INF = 9999999999

# 그냥 시작용
remain = total
cnt1 = 1 
for b in [600, 60, 10]:
    cnt1 += remain // b
    remain %= b
if remain != 0:
    cnt1 = INF

# 처음 버튼 누르고 시작
cnt2 = INF
if total >= 30:
    remain = total - 30
    cnt2 = 1 
    for b in [600, 60, 10]:
        cnt2 += remain // b
        remain %= b
    if remain != 0:
        cnt2 = INF

print(min(cnt1, cnt2))








# import sys
# from collections import deque
# input = sys.stdin.readline

# def bfs(target):
#     """
#     target: 원하는 조리 시간 (초 단위)
#     반환값: 최소 버튼 누름 횟수
#     """
#     q = deque([(0, False, 0)])  # (현재시간, 조리중여부, 버튼누른횟수)
#     visited = set()
#     visited.add((0, False))

#     buttons = [10, 60, 600]  # 10초, 1분, 10분 버튼

#     while q:
#         time, cooking, presses = q.popleft()

#         # 목표 달성 조건: 시간이 정확히 target이고 조리중이어야 함
#         if time == target and cooking:
#             return presses

#         # ① 10초 / 1분 / 10분 버튼
#         for b in buttons:
#             nxt = (time + b, cooking)
#             if nxt not in visited and time + b <= 3600:
#                 visited.add(nxt)
#                 q.append((time + b, cooking, presses + 1))

#         # ② 조리시작 버튼
#         if not cooking:
#             if time == 0:
#                 nxt = (30, True)  # 0초일 땐 30초 세팅 + 조리 시작
#             else:
#                 nxt = (time, True)  # 시간이 있으면 조리 시작
#         else:
#             nxt = (time + 30, True)  # 조리중이면 +30초

#         if nxt[0] <= 3600 and nxt not in visited:
#             visited.add(nxt)
#             q.append((nxt[0], nxt[1], presses + 1))

#     return -1  # 도달 불가 (문제 조건상 나오지 않음)


# # --- 메인 부분 ---
# m, s = map(int, input().strip().split(':'))
# target = m * 60 + s
# print(bfs(target))
