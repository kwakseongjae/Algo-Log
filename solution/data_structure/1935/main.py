# Authored by: kwakseongjae
# Problem: https://www.acmicpc.net/problem/1935
import sys
from collections import deque

# 입력 함수 정의
def input():
    return sys.stdin.readline().rstrip()

N = int(input()) # 피 연산자의 개수
exp = input() # 후위 표기식
num_list = deque([[int(input()) for _ in range(N)]])

op = "+-*/" # 연산자의 종류
stack = []
dic = {} # 문자열과 매칭되는 숫자를 매핑할 수 있는 딕셔너리를 이용

for i in exp:
    if i not in dic and i not in op:
        dic[i] = num_list.popleft() 
        
for i in exp:
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
        
print(f"{stack[0]:.2f}") # 계산 결과를 소숫점 둘째 자리까지 출력