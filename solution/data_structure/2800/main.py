# Authored by: kwakseongjae 
# Problem: https://www.acmicpc.net/problem/2800
import sys
from itertools import combinations

# 입력 함수 정의
def input():
    return sys.stdin.readline().rstrip()

exp = input() # 수식 입력

stack = []
bracket = []
answer = set() # 중복 결과 방지 
for idx, word in enumerate(exp):
    if word == "(":
        stack.append(idx)
    elif word == ")":
        bracket.append((stack.pop(), idx))

for i in range(1, len(bracket) + 1):
    for j in list(combinations(bracket, i)): # 조합을 사용하여 모든 경우의 수 확인
        target = list(exp)
        
        # 괄호 제거
        for k in j:
            target[k[0]] = ""
            target[k[1]] = ""
        answer.add("".join(target))

# 정답 출력
for ans in sorted(list(answer)):
    print(ans)
