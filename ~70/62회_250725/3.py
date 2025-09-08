import sys
input = sys.stdin.readline
from collections import deque

r, c = map(int, input().split())
k = int(input())
room = [[True] * c for _ in range(r)]
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

for _ in range(k):
    br, bc = map(int, input().split())
    room[br][bc] = False
sr, sc = map(int, input().split())
move = list(map(int, input().split()))

def search(sr, sc):
    cr, cc = sr, sc
    room[cr][cc] = False
    idx = 0  # move 리스트 내 인덱스

    while True:
        moved = False
        
        for _ in range(len(move)):
            d = move[idx] - 1
            dx, dy = directions[d]
            
            # 직선 이동
            while True:
                nr = cr + dx
                nc = cc + dy
                if 0 <= nr < r and 0 <= nc < c and room[nr][nc]:
                    cr, cc = nr, nc
                    room[cr][cc] = False
                    moved = True
                else:
                    break  # 이 방향 끝
            
            idx = (idx + 1) % len(move)  # 다음 방향

            if moved:
                break  # 직진이라도 성공했으면 방향 순서 처음부터 다시
        
        if not moved:  # 4방향 다 못 가면 정지
            break
    
    return cr, cc


aa, bb = search(sr, sc)
print(aa, bb)
     