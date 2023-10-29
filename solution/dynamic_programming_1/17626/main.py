# Authored by: kwakseongjae
# Problem: https://www.acmicpc.net/problem/17626
import sys
import math

def input():
    return sys.stdin.readline().rstrip()

n = int(input())
dp = [0] * 50001
INF = float('inf')

dp[0] = 0
dp[1] = 1
for i in range(2, n + 1):
    min_value = INF
    for k in range(1, math.floor(math.sqrt(i)) + 1):
        min_value = min(min_value, dp[i - (k * k)])
    dp[i] = min_value + 1
    
print(dp[n])