# Authored by: kwakseongjae
# Problem: https://www.acmicpc.net/problem/21919
import sys
from math import sqrt

def input():
    return sys.stdin.readline().rstrip()

def GCD(x, y):
    if y == 0:
        return x   
    else:
        return GCD(y, x%y)
    
arr = [0] * 100003
for i in range(2, int(sqrt(1000003)) + 1):
    for j in range(i + i, 1000003, i):
        if arr[j] == 0:
            arr[j] = 1

arr[0] = 1
arr[1] = 1
LCM = 1
N = int(input())
A = list(map(int, input().split()))
answer = []
for i in A:
    if not arr[i]:
        answer.append(i)

if not answer:
    print(-1)
else:
    LCM = answer[0]
    for i in range(1, len(answer)):
        LCM = answer[i] * LCM // GCD(answer[i], LCM)
    print(LCM)