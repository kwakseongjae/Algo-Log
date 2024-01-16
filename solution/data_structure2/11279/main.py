# Authored by: kwakseongjae
# Problem: https://www.acmicpc.net/problem/11279
import sys
import heapq

# 입력 함수 정의
def input():
    return sys.stdin.readline().rstrip()

N = int(input())

heap = []
for _ in range(N):
    x = int(input())
    # minheap을 활용하기 위해 push할 때 음수로 변환하고 pop할 때 양수로 변환
    if x == 0:
        if heap:
            print(-heapq.heappop(heap))
        else:
            print(0)
    heapq.heappush(heap, -x)
