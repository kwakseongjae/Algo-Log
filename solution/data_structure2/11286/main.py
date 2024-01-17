# Authored by: kwakseognjae
# Problem: https://www.acmicpc.net/problem/11286
import sys
import heapq

# 입력 함수 정의
def input():
    return sys.stdin.readline().rstrip()

N = int(input())

abs_heap = []
for i in range(N):
    num = int(input())
    
    # 받은 값이 0이 아닌 경우
    if num:
        # 절대값을 기준으로 최소힙 구성
        heapq.heappush(abs_heap, [abs(num), num])
    # 받은 값이 0인 경우
    else:
        if abs_heap:
            print(heapq.heappop(abs_heap)[1])
        else:
            print(0)