# Authored by: kwakseongjae
# Problem: https://www.acmicpc.net/problem/4134
# Reference: https://velog.io/@www-jong/%EB%B0%B1%EC%A4%80-4134.-%EB%8B%A4%EC%9D%8C%EC%86%8C%EC%88%98-Python

N = int(input())

def check(num):
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

for _ in range(N):
    n = int(input())
    while True:
        if n==0 or n==1:
            print(2)
            break
        if check(n):
            print(n)
            break
        n += 1