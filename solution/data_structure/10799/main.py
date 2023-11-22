# Authored by: kwakseongjae
# Problem: https://www.acmicpc.net/problem/10799
import sys

# 입력 함수 정의
def input():
    return sys.stdin.readline().rstrip()

exp = input() # 쇠막대기와 레이저의 배치를 나타내는 괄호 표현

stack = []
result = 0
for i, v in enumerate(exp):
    if v == "(":
        stack.append("(")
    elif v == ")":
        if exp[i-1] == "(":
            stack.pop()
            result += len(stack)
        else:
            stack.pop()
            result += 1

print(result)