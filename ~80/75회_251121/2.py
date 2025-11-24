import sys
input = sys.stdin.readline
from collections import defaultdict

a = input().rstrip()
l = len(a)

dp = [[] * (l + 1) for _ in range(l + 1)]
dic = defaultdict(int)

def aa():
    b =  a[:l//2 + 1]
    