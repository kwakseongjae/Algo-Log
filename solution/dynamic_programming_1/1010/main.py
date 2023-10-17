# Authored by: kwakseongjae
# Problem: https://www.acmicpc.net/problem/1010
import sys

def input():
    return sys.stdin.readline().rstrip()

T = int(input())

dp = [[0 for _ in range(31)] for _ in range(31)]
dp[0][0] = 1

for i in range(0, 31):
    dp[i][0] = 1
    for j in range(1, 31):
        dp[i][j] = dp[i - 1][j] + dp[i - 1][j - 1]
        
for _ in range(T):
    N, M = map(int, input().split())
    print(dp[M][N])