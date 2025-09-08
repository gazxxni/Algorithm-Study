import sys
input = sys.stdin.readline

n, m, x, y = map(int, input().split())
road = []

for _  in range(m):
    a, b, c = map(int, input().split())
    road[a] = (b, c)
    road[b] = (a, c)
    
