# Authored by: kwakseongjae
# Problem: https://www.acmicpc.net/problem/16954
import sys
from collections import deque

def input():
    return sys.stdin.readline().rstrip()

board = [list(input()) for _ in range(8)]

def bfs(board):
    end = (0, 7)
    queue = deque()
    queue.append((7, 0, 0))
    visit = [[False] * 8 for _ in range(8) for _ in range(9)]
    visit[0][7][0] = True
    
    dx = [0, -1, 1, 0, 0, -1, 1, 1, -1]
    dy = [0, 0, 0, -1, 1, -1, 1, -1, 1]
    
    result = 0
    while queue:
        y, x, time = queue.popleft()
        if y == end[0] and x == end[1]:
            result = 1
            break
        for i in range(9):
            nx = x + dx[i]
            ny = y + dy[i]
            ntime = min(time + 1, 8)
            
            if ny<0 or ny>=8 or nx<0 or nx>=8: continue
            if ny-time>=0 and board[ny-time][nx]=='#': continue
            if ny-ntime>=0 and board[ny-ntime][nx]=='#': continue
            if visit[ntime][ny][nx]: continue
            
            visit[ntime][ny][nx] = True
            queue.append((ny, nx, ntime))
    return result

print(bfs(board))