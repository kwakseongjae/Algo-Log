# Authored by: kwakseongjae
# Problem: https://www.acmicpc.net/problem/4179
import sys
from collections import deque

def input():
    return sys.stdin.readline().rstrip()

r, c = map(int, input().split())
board = [[-1] * (c + 2) for _ in range(r + 2)]
visit = [[False] * (c + 2) for _ in range(r + 2)]

queue = deque()
fire_queue = deque()

dx = [-1, 1 , 0, 0]
dy = [0, 0, -1, 1]

for i in range(1, r + 1):
    line = input()
    for j in range(1, c + 1):
        if line[j -1] == "#":
            board[i][j] == 1
        elif line[j -1] == ".":
            board[i][j] == 0
        elif line[j -1] == "J":
            board[i][j] == 0
            queue.append([i, j])
        elif line[j -1] == "F":
            board[i][j] = 2
            fire_queue.append([i, j])

def check(current, board):
    y, x = current 
    return board[y][x] == -1

def bfs(queue, cnt):
    global r, c
    next_queue = deque()
    while queue:
        y, x = queue.popleft()
        if board[y][x] == 2:
            continue
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if ny < 0 or ny >= r + 2 or nx < 0 or nx >= c + 2:
                continue
            if board[ny][nx] == 1 or board[ny][nx] == 2: 
                continue
            if visit[ny][nx]: 
                continue
            if check((ny,nx), board):
                return True, next_queue
            next_queue.append([ny, nx])
            visit[ny][nx] = True
    return False, next_queue

def fire_bfs(queue):
    global r, c
    next_queue = deque()
    while queue:
        y, x = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if ny <= 0 or ny >= r + 1 or nx <= 0 or nx >= c + 1:
                continue
            if board[ny][nx] == 1 or board[ny][nx] == 2: 
                continue
            next_queue.append([ny, nx])
            board[ny][nx] = 2
    return next_queue

def solution():
    global q, fire_queue
    cnt = 0
    while True:
        cnt += 1
        check, q = bfs(q, cnt)
        if check:
            return cnt
        if not q:
            return 'IMPOSSIBLE'
        fire_queue = fire_bfs(fire_queue)
    return 'IMPOSSIBLE'

print(solution())