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
        # heap의 크기를 N개로 유지
        if len(heap) < N:
                heapq.heappush(heap, number)
        # 우선순위 큐의 최솟값을 제거하고 현재 확인하고 있는 숫자를 우선순위 큐에 삽입    
        else: 
            if heap[0] < number:
                print(heapq.heappop(heap))
                heapq.heappush(heap, number)

print(heap[0])

