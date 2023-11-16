# Authored by: kwakseongjae
# Problem: https://www.acmicpc.net/problem/2812
import sys

def input():
    return sys.stdin.readline().rstrip()

n, k = map(int, input().split())
num = list(input())
t = k
stack = []

for i in range(n):
    while k > 0 and stack:
        if stack[-1] < num[i]:
            stack.pop()
            k -= 1
        else:
            break
    stack.append(num[i])
    
print(*stack[:(n - t)], sep='')