import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n, r = map(int, input().split())
tree = [[] for _ in range(n+1)]

for _ in range(n-1):
    a, b, d = map(int, input().split())
    tree[a].append((b, d))
    tree[b].append((a, d))

pillar = r
len_pillar = 0
prev = 0

while True:
    if prev == 0:
        cnt = len(tree[pillar])
    else:
        cnt = len(tree[pillar]) - 1

    if cnt >= 2 or cnt == 0:
        break

    for nxt, w in tree[pillar]:
        if nxt != prev:
            len_pillar = len_pillar + w
            prev = pillar
            pillar = nxt
            break

def dfs(node, dist, parent):
    ret = dist
    for nxt, w in tree[node]:
        if nxt != parent:
            cand = dfs(nxt, dist + w, node)
            if cand > ret:
                ret = cand
    return ret

if prev == 0:
    cnt = len(tree[pillar])
else:
    cnt = len(tree[pillar]) - 1

if cnt == 0:
    leaf = 0
else:
    leaf = 0
    for nxt, w in tree[pillar]:
        if nxt != prev:
            cand = dfs(nxt, w, pillar)
            if cand > leaf:
                leaf = cand

print(len_pillar, leaf)
