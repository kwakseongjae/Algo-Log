# Authored by: kwakseongjae
# Problem: https://www.acmicpc.net/problem/1918
import sys

# 입력 함수 정의
def input():
    return sys.stdin.readline().rstrip()

exp = input() # 중위 표현식

stack = []
answer = ""
for ch in exp:
    if ch.isalpha():
        answer += ch
    else:
        if ch == "(":
            stack.append(ch)
        elif ch in ("+", "-"):
            while stack and stack[-1] != "(":
                answer += stack.pop()
            stack.append(ch)
        elif ch in ("/", "*"):
            while stack and stack[-1] in ("/", "*"):
                answer += stack.pop()
            stack.append(ch)
        elif ch == ")":
            while stack and stack[-1] != "(":
                answer += stack.pop()
            stack.pop()

while stack:
    answer += stack.pop()

# 정답 출력
print(answer)