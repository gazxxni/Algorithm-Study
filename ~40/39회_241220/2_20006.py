import sys

p, m = map(int, input().split())
room = []

for _ in range(p):  # O(p)
    level, name = input().split()

    if not room:
        room.append([[int(level), name]])  # 새로운 방 생성, 플레이어를 방에 추가
        continue

    enter = False  # 방에 입장 여부를 판단

    for i in room:  # 방의 최대 수는 p -> O(p)
        # 방에 자리가 있고, 범위를 만족하는 경우
        if len(i) < m and i[0][0] - 10 <= int(level) <= i[0][0] + 10:
            i.append([int(level), name])  # 플레이어 추가
            enter = True  # 방에 입장했음을 표시
            break

    if not enter:  # 방을 찾지 못한 경우 새로운 방 생성
        room.append([[int(level), name]])

    # 이중 for문으로 O(p^2)

for i in room: # 각 방의 플레이어를 이름 순으로 정렬
    i.sort(key=lambda x: x[1])

    # 방의 최대 수는 p -> O(plogp)

for i in room:  # 모든 플레이어를 한번씩만 처리하기 때문에 O(p)
    if len(i) == m:  # 방이 시작되면
        print('Started!')
    else:  # 방이 대기 중이면
        print('Waiting!')

    for a, b in i:
        print(a, b)
