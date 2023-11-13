# Authored by: kwakseongjae
# Problem: https://www.acmicpc.net/problem/19598
import sys
import heapq

def input():
    return sys.stdin.readline().rstrip()

n = int(input())
_list = sorted([list(map(int, input().split())) for _ in range(n)])

heap = [_list[0][1]]
for i in range(1, n):
    if heap[0] > _list[i][0]:
        heapq.heappush(heap, _list[i][1])
    else:
        heapq.heappop(heap)
        heapq.heappush(heap, _list[i][1])

print(len(heap))