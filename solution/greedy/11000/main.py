# Authored by: kwakseongjae
# Problem: https://www.acmicpc.net/problem/11000
import sys
import heapq

def input():
    return sys.stdin.readline().rstrip()

N = int(input())
lecture = []
for _ in range(N):
    heapq.heappush(lecture, list(map, input().split()))
    
end_points = []
while lecture:
    l = heapq.heappop(lecture)
    if end_points:
        if l[0] >= end_points[0]:
            heapq.heappop(end_points)
        heapq.heappop(end_points, l[1])
        
    print(len(end_points))