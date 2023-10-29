# Authored by: kwakseongjae
# Problem: https://www.acmicpc.net/problem/11653
import sys

def input():
    return sys.stdin.readline().rstrip()

N = int(input())
X = N
for i in range(2, N + 1):
    if X == 1:
        break
    while X % i == 0:
        X //= i
        print(i)