# Authored by: kwakseongjae
# Problem: https://www.acmicpc.net/problem/18258
import sys
from collections import deque

def input():
    return sys.stdin.readline().rstrip()

N = int(input())

queue = deque()
for i in range(N):
    cmd = input().split()
    if cmd[0] == "push":
        queue.append(cmd[1])
    elif cmd[0] == "pop":
        if queue:
            print(queue.popleft())
        else:
            print(-1)
    elif cmd[0] == "siz":
        print(len(queue))
    elif cmd[0] == "front":
        if queue:
            print(queue[0])
        else:
            print(-1)
    elif cmd[0] == "back":
        if queue:
            print(queue[-1])
        else:
            print(-1)
    elif cmd[0] == "empty":
        if not queue:
            print(-1)
        else:
            print(0)
            