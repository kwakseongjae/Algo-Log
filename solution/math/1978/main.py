# Authored by : gusdn3477
# Problem: https://www.acmicpc.net/problem/1978
import sys
from math import sqrt

def input():
    return sys.stdin.readline().rstrip()

N = int(input())
arr = list(map(int, input().split()))

prime = [1] * 1005
prime[0] = 0
prime[1] = 0
cnt = 0
for i in range(2, int(sqrt(1005)+1)):
    for j in range(i*2, 1005, i):
        if prime[j] == 1:
            prime[j] = 0
for i in arr:
    if prime[i] == 1:
        cnt += 1

print(cnt)