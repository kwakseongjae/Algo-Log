# Authored by: kwakseongjae
# Problem: https://www.acmicpc.net/problem/1874
import sys

# 입력 함수 정의
def input():
    return sys.stdin.readline().rstrip()

n = int(input()) # 입력받는 숫자의 개수
stack = []
answer = []
find = True

now = 1
for _ in range(n):
    num = int(input())
    
    # Push
    while now <= num:
        stack.append(now)
        answer.append("+")
        now += 1
    # Pop
    if stack[-1] == num:
        stack.pop()
        answer.append("-")
    # 불가능한 경우
    else: 
        find = False

# 정답 출력
if not find:
    print("NO")
else:
    print("\n".join(map(str, answer)))

