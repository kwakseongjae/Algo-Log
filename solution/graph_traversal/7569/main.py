# Authored by: kwakseongjae
# Problem: https://www.acmicpc.net/problem/7569
import sys
from collections import deque

def input():
    return sys.stdin.readline().rstrip()

M, N, H = map(int, input().split())

nx = [-1, 0, 1, 0, 0, 0]
ny = [0, -1, 0, 1, 0, 0]
nz = [0, 0, 0, 0, -1, 1]

queue = deque()
arr = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]

def checkMap():
    for z in range(H):
        for x in range(N):
            for y in range(M):
                if arr[z][x][y] == 0:
                    return False
    return True

def BFS():
    while queue:
        q = queue.popleft()
        z, x, y = q[0]
        for i in range(6):
            dx = x + nx[i]
            dy = y + ny[i]
            dz = z + nz[i]
            if dx < 0 or dx >= N or dy < 0 or dy >= M or dz < 0 or dz >= H:
                continue
            if arr[dz][dx][dy] == 0:
                arr [dz][dx][dy] = 1
                queue.append((dz, dx, dy), q[1]+ 1)
    if checkMap():
        return q[1]
    return -1

for z in range(H):
    for x in range(N):
        for y in range(M):
            if arr[z][x][y] == 1:
                arr[z][x][y] = 1
                queue.append(((z, x, y), 0))

answer = BFS()
print(answer)                