# Authored by: kwakseongjae
# Problem: https://www.acmicpc.net/problem/5618
import sys

def input():
    return sys.stdin.readline().rstrip()

def GCD(x, y):
    if y == 0: 
        return x
    else:
        return GCD(y, x%y)
    
n = int(input())
arr = list(map(int, input().split()))

gdc = arr[0]
result = []
for i in range(1, n):
    gcd = GCD(gcd, arr[i])
    
x = 1
while x * x <= gcd:
    if gcd % x == 0:
        result.append(x)
        if x * x != gcd:
            result.append(gcd // x)
    x += 1
    
result.sort()
print(*result)

