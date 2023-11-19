# Authored by: kwakseongjae
# Problem: https://www.acmicpc.net/problem/2164
import sys
from collections import deque

# 입력 함수 정의
def input():
    return sys.stdin.readline().rstrip()

N = int(input()) # 카드의 수

queue = deque([i + 1 for i in range(N)])
while queue:
    a = queue.popleft()
    if not queue:
        print(a)
        break
    b = queue.popleft()
    queue.append(b)
    

