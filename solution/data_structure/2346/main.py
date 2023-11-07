# Authored by: kwakseongjae
# Problem: https://www.acmicpc.net/problem/2346
import sys
from collections import deque
def input():
    return sys.stdin.readline().rstrip()

N = int(input())
queue1 = deque(list(map(int, input().split())))
queue2 = deque([i for i in range(1, N + 1)])

while queue1:
    q = queue1[0]
    if q > 0:
        queue1.popleft()
        queue1.rotate(-q + 1)
        print(queue2.popleft())
        queue2.rotate(-q + 1)
    else:
        queue1.popleft()
        queue1.rotate(-q)
        print(queue2.popleft())
        queue2.rotate(-q)