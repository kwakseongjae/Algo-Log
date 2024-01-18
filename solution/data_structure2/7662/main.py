# Authored by: kwakseongjae
# Problem: https://www.acmicpc.net/problem/7662
import sys
import heapq
from collections import defaultdict

# 입력 함수 정의
def input():
    return sys.stdin.readline().rstrip()

T = int(input())
for _ in range(T):
    K = int(input())
    max_queue = []
    min_queue = []
    visited = [False] * K

    for i in range(K):
        operator, number = input().split()
        if operator == "I":
            number = int(number)
            heapq.heappush(max_queue, (-number, i))
            heapq.heappush(min_queue, (number, i))
            visited[i] = True
        else:
            if number == "1":
                while max_queue and not visited[max_queue[0][1]]:
                    heapq.heappop(max_queue)
                if max_queue:
                    visited[max_queue[0][1]] = False
                    heapq.heappop(max_queue)
            else:
                while min_queue and not visited[min_queue[0][1]]:
                    heapq.heappop(min_queue)
                if min_queue:
                    visited[min_queue[0][1]] = False
                    heapq.heappop(min_queue)
    
    while min_queue and not visited[min_queue[0][1]]:
        heapq.heappop(min_queue)
    while max_queue and not visited[max_queue[0][1]]:
        heapq.heappop(max_queue)

    # 각각의 테스트케이스에 대한 출력문
    if min_queue and max_queue:
        max_num = -max_queue[0][0]
        min_num = min_queue[0][0]
        print(max_num, min_num)
    else:
        print("EMPTY")