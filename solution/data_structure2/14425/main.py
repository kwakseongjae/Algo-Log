# Authored by: kwakseongjae
# Problem: https://www.acmicpc.net/problem/14425
import sys
from collections import deque

def input():
    return sys.stdin.readline().rstrip()

N, M = map(int, input().split)

answer = 0
dict = {}
for i in range(N):
    a = input()
    dict[a] = 1
for i in range(M):
    a = input()
    if a in dict:
        answer += 1

print(answer)