# Authored by: kwakseongjae
# Problem: https://www.acmicpc.net/problem/1935
import sys
from collections import deque

def input():
    return sys.stdin.readline().rstrip()

N = int(input())
arr = input()

op = "+-*/"
stack = []
dic = {}
num = deque()

for i in range(N):
    num.append(int(input()))

for i in arr:
    if i not in dic and i not in op:
        dic[i] = num.popleft()
        
for i in arr:
    if i not in op:
        stack.append(dic[i])
    else:
        if i == "+":
            a = stack.pop()
            b = stack.pop()
            stack.append(b + a)
        elif i == "-":
            a = stack.pop()
            b = stack.pop()
            stack.append(b - a)
        elif i == "*":
            a = stack.pop()
            b = stack.pop()
            stack.append(b * a)
        elif i == "/":
            a = stack.pop()
            b = stack.pop()
            stack.append(b / a)
        
print(f"{stack[0]:.2f}")