# Authored by : kwakseongjae
# Problem: https://www.acmicpc.net/problem/1978
# Reference: https://yuna0125.tistory.com/187

import sys
from math import sqrt

# 입력 함수 정의
def input():
    return sys.stdin.readline().rstrip()

N = int(input())
num_list = list(map(int, input().split()))
result = 0

for num in num_list:
    cnt = 0
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                cnt += 1
        
        if cnt == 0:
            result += 1
    
print(result)