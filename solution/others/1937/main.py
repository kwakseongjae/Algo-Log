# Authored by: kwakseongjae
# Problem: https://www.acmicpc.net/problem/1937
# Reference: https://kyun2da.github.io/2021/04/04/panda/

import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

# 방향배열: 상하좌우
direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]

n = int(input())
forest = [list(map(int, input().split())) for _ in range(n)]
dp = [[0] * n for _ in range(n)]

def dfs(y, x):
    if dp[y][x]:
        return dp[y][x]
    dp[y][x] = 1
    for dy, dx in direction:
        ny, nx = y + dy, x + dx
        if 0 <= ny < n and 0 <= nx < n:
            if forest[ny][nx] > forest[y][x]:
                dp[y][x] = max(dp[y][x], dfs(ny, nx) + 1)
    return dp[y][x]

answer = 0
for i in range(n):
    for j in range(n):
        answer = max(answer, dfs(i, j))
print(answer)