# Authored by: kwakseongjae
# Problem: https://www.acmicpc.net/problem/1158
import sys
from collections import deque

# 입력 함수 정의
def input():
    return sys.stdin.readline().rstrip()

N, K = map(int, input().split()) # N: 사람의 수, K: 제거해야하는 사람의 순서
queue = deque([i + 1 for i in range(N)])

result = []
while queue:
    queue.rotate(-K) # 왼쪽으로 K만큼 회전
    result.append(queue.pop())
    
print("<" + ", ".join(map(str, result)) + ">")
