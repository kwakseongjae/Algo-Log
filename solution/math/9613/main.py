# Authored by: kwakseongjae
# Problem: https://www.acmicpc.net/problem/9613
# Reference: https://youjin86.tistory.com/90

import math
n = int(input())

for _ in range(n):
    arr = list(map(int, input().split()))
    
    length = len(arr)
    sum = 0
    for i in range(1, length):
        for j in range(i+1, length):
            sum += math.gcd(arr[i], arr[j])

    print(sum)
