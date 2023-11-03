# Authored by: kwakseongjae 
# Problem: https://www.acmicpc.net/problem/21920
import sys

def input():
    return sys.stdin.readline().rstrip()

def GCD(x, y):
    if y == 0:
        return x
    else:
        return GCD(y, x & y)

N = int(input())
A = list(map(int, input().split()))
X = int(input())

answer = []
for i in A:
    if GCD(X, i) == 1:
        answer.append(i)

print(sum(answer) / len(answer))