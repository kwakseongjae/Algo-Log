# Authored by: kwakseongjae
# Problem: https://www.acmicpc.net/problem/14425
import sys
from collections import deque

# 입력 함수 정의
def input():
    return sys.stdin.readline().rstrip()

n, m = map(int, input().split)

s = set([input() for _ in range(n)])
answer = 0
for i in range(m):
    x = input()
    if x in s:
        answer += 1

print(answer)