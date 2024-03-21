# Authored by: kwakseongjae 
# Problem: https://www.acmicpc.net/problem/21920
# Reference: https://aldrn29.tistory.com/123

import math

N = int(input())
A = list(map(int, input().split()))
X = int(input())
result = 0
cnt = 0

for num in A :
    if math.gcd(num, X) == 1 :
        result += num
        cnt += 1

print(result / cnt)