# Authored by: kwakseongjae
# Problem: https://www.acmicpc.net/problem/10828
import sys

# 입력 함수 정의
def input(): 
    return sys.stdin.realine().rstrip()

N = int(input()) # 명령어의 수 

stack = []
for i in range(N):
    cmd = input().split()
    
    if cmd[0] == "push":
        stack.append(cmd[1])
    elif cmd[0] == "pop":
        if len(stack) == 0:
            print(-1)
        else:
            print(stack.pop())
    elif cmd[0] == "size":
        print(len(stack))
    elif cmd[0] == "empty":
        print(0 if len(stack) else 1)
    elif cmd[0] == "top":
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])