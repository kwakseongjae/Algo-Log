# Authored by: kwakseongjae
# Problem: https://www.acmicpc.net/problem/2164
import sys
from collections import deque

def input():
    return sys.stdin.readline().rstrip()

N = int(input())

queue = deque()
for i in range(1, N + 1):
    queue.append(i)
    
while True:
    a = queue.popleft()
    if not queue:
        print(a)
        break
    b = queue.popleft()
    queue.append(b)
    

