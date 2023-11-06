# Authored by: kwakseongjae
# Problem: https://www.acmicpc.net/problem/1966
import sys
from collections import deque

def input():
    return sys.stdin.readline().rstrip()

T = int(input())
for i in range(T):
    queue1 = deque()
    queue2 = deque()
    cnt = 1
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    for j in range(len(arr)):
        queue1.append(arr[j])
        queue2.append(j)
    while True:
        if queue1[0] == max(queue1):
            if queue2[0] == M:
                print(cnt)
                break
            else:
                queue1.popleft()
                queue2.popleft()
        else:
            queue1.rotate(-1)
            queue2.rotate(-1)                