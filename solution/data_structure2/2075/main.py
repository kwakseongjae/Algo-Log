# Authored by : kwakseongjae
# Link : https://www.acmicpc.net/problem/2075
import heapq
import sys

# 입력 함수 정의 
def input():
    return sys.stdin.readline().rstrip()

N = int(input())

heap = []
for _ in range(N):
    numbers = list(map(int, input().split()))
    for number in numbers:
        if len(heap) < N: # heap의 크기를 N개로 유지
                heapq.heappush(heap, number)
        else:
            if heap[0] < number:
                print(heapq.heappop(heap))
                heapq.heappush(heap, number)

print(heap[0])

