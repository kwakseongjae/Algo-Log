# Authored by: kwakseongjae
# Problem: https://www.acmicpc.net/problem/5347
# Reference: https://alpyrithm.tistory.com/141

def gcd(a, b):
    while b:
        mod = b
        b = a % b
        a = mod
    return a

n = int(input())
for _ in range(n):
    a, b = map(int, input().split())
    print(a*b // gcd(a, b))