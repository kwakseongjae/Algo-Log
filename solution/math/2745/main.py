# Authored by: kwakseongjae
# Problem: https://www.acmicpc.net/problem/2745
# Reference: https://newl.yammyblock.com/46

import sys

# 입력 함수 정의
def input():
    return sys.stdin.readline().rstrip()

NUM_STR="0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

N, B = input().split()
N = N[::-1]
answer = 0
for idx, num in enumerate(N):
    answer += NUM_STR.find(num) * int(B)**idx

print(answer)