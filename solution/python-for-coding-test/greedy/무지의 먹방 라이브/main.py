# Authored by: kwakseonjae
# Problem: https://school.programmers.co.kr/learn/courses/30/lessons/42891?language=python3
# Reference: https://kjhoon0330.tistory.com/entry/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%EB%AC%B4%EC%A7%80%EC%9D%98-%EB%A8%B9%EB%B0%A9-%EB%9D%BC%EC%9D%B4%EB%B8%8C-Python

from heapq import heappush, heappop

def solution(food_times, k):
    # 방송 중단 전 음식을 다 먹는 경우
    if sum(food_times) <= k:
        return -1
    
    food_heap = []
    length = len(food_times) # 남은 음식 개수
    for idx in range(length):
        heappush(food_heap, [food_times[idx], idx + 1]);
    
    time = 0
    while (food_heap[0][0] - time) * length < k:
        k -= (food_heap[0][0] - time) * length
        time += (food_heap[0][0] - time)
        length -= 1
        heappop(food_heap)
        
    result = sorted(food_heap, key = lambda x : x[1]) # index를 기준으로 heap을 다시 정렬
    answer = result[k % length][1]
    
    return answer