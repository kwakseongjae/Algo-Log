# Authored by: kwakseongjae
# Problem: https://www.acmicpc.net/problem/7662
import sys
import heapq
from collections import defaultdict

def input():
    return sys.stdin.readline().rstrip()

for T in range(int(input())):
    max_queue = []
    min_queue = []
    total_ele_cnt = 0
    ele_cnt = defaultdict(int)
    for _ in range(int(input())):
        operator, number = input().split()
        if operator == "I":
            number = int(number)
            heapq.heappush(max_queue, -number)
            heapq.heappush(min_queue, number)
            ele_cnt[number] += 1
            total_ele_cnt += 1
        else:
            if total_ele_cnt > 0:
                if number == "1":
                    while True:
                        del_num = -heapq.heappop(max_queue)
                        if ele_cnt[del_num]:
                            ele_cnt[del_num] -= 1
                            break
                else:
                    while True:
                        del_num = heapq.heappop(min_queue)
                        if ele_cnt[del_num]:
                            ele_cnt[del_num] -= 1
                            break
                total_ele_cnt -= 1
    
    if total_ele_cnt:
        while True:
            max_value = -heapq.heappop(max_queue)
            if ele_cnt[max_value]:
                break
        while True:
            min_value = heapq.heappop(min_queue)
            if ele_cnt[min_value]:
                break
        print(max_value, min_value)
    else:
        print("EMPTY")    
    