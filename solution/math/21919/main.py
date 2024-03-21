# Authored by: kwakseongjae
# Problem: https://www.acmicpc.net/problem/21919
# Reference: https://wizdom.tistory.com/173

import sys
input = sys.stdin.readline

def is_prime_num(num):
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

N = int(input())
num_list = set(list(map(int, input().split())))

answer = 1
for num in num_list:
    if is_prime_num(num):
        answer *= num

if answer == 1:
    print(-1)
else: 
    print(answer)