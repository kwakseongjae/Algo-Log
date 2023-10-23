# Authored by: kwakseongjae
# Problem: https://www.acmicpc.net/problem/11279
import sys
import heapq

def input():
    return sys.stdin.readline().rstrip()

N = int(input())

heap = []
for i in range(N):
    x = int(input())
    if x == 0:
        if heap:
            print(-heapq.heappop(heap))
        else:
            print(0)
    heapq.heappush(heap, -x)
