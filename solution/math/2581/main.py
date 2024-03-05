# Authored by : kwakseongjae
# Problem: https://www.acmicpc.net/problem/2581
# Reference: https://yuna0125.tistory.com/36

import sys
from math import sqrt

# 입력 함수 정의
def input():
    return sys.stdin.readline().rstrip()

M = int(input())
N = int(input())
prime_list = []

for num in range(M, N+1):
    if num == 1:
        pass
    elif num == 2:
        prime_list.append(num)
    else:
        for i in range(2, num):
            if num % i==0:
                break
            elif i == num-1:
                prime_list.append(num)

if prime_list:
    print(sum(prime_list))
    print(min(prime_list))
else:
    print('-1')