import sys, heapq
input = sys.stdin.readline

n = int(input())
arr = [int(input()) for _  in range(n)]

h = []

for i in arr:
    heapq.heappush(h, i)
    
cnt = 0

while len(h) > 1:

    a = heapq.heappop(h)
    b = heapq.heappop(h)
    c = a + b
    cnt += c
        
    heapq.heappush(h, c)

print(cnt)