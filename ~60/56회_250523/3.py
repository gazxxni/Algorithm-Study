n = int(input())
board = [[None] * 20 for _ in range(20)]

directions = [(0,1), (1,0), (1,1), (1,-1)]

result = -1
aa = True

for i in range(1, n+1):
    r, c = map(int, input().split())

    board[r][c] = aa

    for dx, dy in directions:
        cnt = 1

        nr, nc = r + dx, c + dy

        while 1 <= nr <= 19 and 1 <= nc <= 19 and board[nr][nc] == aa:
            cnt += 1
            nr += dx
            nc += dy


        nr, nc = r - dx, c - dy

        while 1 <= nr <= 19 and 1 <= nc <= 19 and board[nr][nc] == aa:
            cnt += 1
            nr -= dx
            nc -= dy

        if cnt == 5:
            prev_r, prev_c = r - dx * 5, c - dy * 5
            next_r, next_c = r + dx * 5, c + dy * 5

            prev_check = (1 <= prev_r <= 19 and 1 <= prev_c <= 19 and board[prev_r][prev_c] == aa)
            next_check = (1 <= next_r <= 19 and 1 <= next_c <= 19 and board[next_r][next_c] == aa)

            if not prev_check and not next_check:
                result = i
                break

    if result != -1:
        break

    aa = not aa



print(result)