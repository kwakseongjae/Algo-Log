# Authored by: kwakseongjae
# Problem: https://www.acmicpc.net/problem/22864
# Reference: https://yuna0125.tistory.com/107

import sys

# 입력 함수 정의
def input():
    return sys.stdin.readline().rstrip()

A, B, C, M = map(int, input().split())

work = 0
hour = 24
x = 0 # 피로도
while hour:
    hour -= 1
    if x + A <= M:
        x += A
        work += B
    
    else:
        x -= C
        if x < 0:
            x = 0

print(work)