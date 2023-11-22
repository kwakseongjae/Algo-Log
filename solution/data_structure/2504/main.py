# Authored by: kwakseongjae
# Problem: https://www.acmicpc.net/problem/2504
import sys

# 입력 함수 정의
def input():
    return sys.stdin.readline().rstrip()

str = input() # 괄호열을 나타내는 문자열

stack = []
answer = 0
tmp = 1 # answer에 더해주기 전 값을 저장하는 임시 변수
for i in range(len(str)):
    if str[i] == "(":
        stack.append(str[i])
        tmp *= 2
    elif str[i] == "[":
        stack.append(str[i])
        tmp *= 3
    elif str[i] == ")":
        if not stack or stack[-1] == "[":
            answer = 0
            break
        if str[i-1] == "(":
            answer += tmp
        stack.pop()
        tmp //= 2
    else:
        if not stack or stack[-1] == "(":
            answer = 0
            break
        if str[i-1] == "[":
            answer += tmp
        stack.pop()
        tmp //= 3

# 정답 출력
if stack:
    print(0)
else:
    print(answer)
            
