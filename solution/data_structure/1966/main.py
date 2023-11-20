# Authored by: kwakseongjae
# Problem: https://www.acmicpc.net/problem/1966
import sys
from collections import deque

# 입력 함수 정의
def input():
    return sys.stdin.readline().rstrip()

T = int(input()) # 테스트 케이스의 수

for i in range(T):
    N, M = map(int, input().split()) # N: 문서의 수, M: 궁금한 문서의 현재 위치
    priority = deque(list(map(int, input().split()))) # N개 문서의 중요도
    
    cnt = 0
    while True:
        best = max(priority)  
        front = priority.popleft() 
        M -= 1
                     
        if best == front: # 뽑은 숫자가 제일 큰 숫자인 경우
            cnt += 1 
            if M < 0: 
                print(cnt)
                break
        else:   # 뽑은 숫자가 제일 큰 숫자가 아닌 경우
            priority.append(front) 
            if M < 0 :  # 제일 앞에서 뽑히면
                M = len(priority) - 1 # 제일 뒤로 이동