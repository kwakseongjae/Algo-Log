# Authored by: kwakseongjae
# Problem: https://www.acmicpc.net/problem/1158
import sys
from collections import deque

def input():
    return sys.stdin.readline().rstrip()

N, K = map(int, input().split())
_list = []
queue = deque([i + 1 for i in range(N)])

while queue:
    queue.rotate(-K)
    _list.append(queue.pop())
    
print("<" + ", ".join(map(str, _list)) + ">")
