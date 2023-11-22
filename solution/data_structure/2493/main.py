# Authored by: kwakseongjae
# Problem: https://www.acmicpc.net/problem/2493
import sys

# 입력 함수 정의
def intput():
    return sys.stdin.readline().rstrip()

N = int(input()) # 탑의 수
top_list = list(map(int,input().split())) # 탑의 높이 리스트

stack = []
answer= [0] * N
for i in range(len(top_list)):
    while stack: # 현재 탐색하고 있는 탑의 높이가 Stack TOP의 높이보다 크다면
        if top_list[stack[-1][0]] < top_list[i]:
            stack.pop()
        else: # 현재 탐색하고 있는 탑의 높이가 Stack TOP의 높이보다 작다면
            answer[i] = stack[-1][0] + 1
            break
    stack.append((i, top_list[i]))

# 정답 출력
print(*answer)