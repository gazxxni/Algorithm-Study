import sys

while True:

    a = list(input())

    if int(a) == 0:
        break

def dfs(a):

    for i in range(len(a)):
        