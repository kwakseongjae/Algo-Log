# Authored by: kwakseongjae
# Problem: https://www.acmicpc.net/problem/5618
# Reference: https://michelangeloo.tistory.com/32

import sys

# 입력 함수 정의
def input():
    return sys.stdin.readline().rstrip()

n = int(input())
num_list = list(map(int, input().split()))

min_v = min(num_list)
for i in range(1, min_v + 1):
    cnt = 0
    for num in num_list:
        if num % i == 0:
            cnt += 1
        else:
            break
    if cnt == n:
        print(i)
