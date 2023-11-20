# Authored by: kwakseongjae
# Problem: https://www.acmicpc.net/problem/2346
import sys
from collections import deque

#입력 함수 정의
def input():
    return sys.stdin.readline().rstrip()

N = int(input()) # 풍선의 수
queue = deque(enumerate(map(int, input().split()))) # (인덱스, 값) 구조로 풍선 정보 저장

answer = []
while queue:
    idx,num = queue.popleft()
    answer.append(idx+1)
    if num > 0:
        queue.rotate(-(num-1))
    elif num < 0:
        queue.rotate(-num)

print(' '.join(map(str,answer)))
