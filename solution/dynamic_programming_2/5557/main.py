# Authored by: kwakseongjae
# Problem: https://www.acmicpc.net/problem/5557
import sys

def input():
    return sys.stdin.readline().rstrip()

N = int(input())
numList = list(map(int, input().split()))

dp = [[0] * 21 for _ in range(N - 1)]
dp[0][[numList[0]]] = 1

for i in range(1, N - 1):
    for j in range(21):
        if dp[i -1][j] <= 0:
            continue
        for op in (1, -1):
            temp = j + op * numList[i]
            if 0 <= temp < 21:
                dp[i][temp] += dp[i -1][j]

answer = dp[N - 2][numList[N - 1]]
print(answer)