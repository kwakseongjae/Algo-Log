# Author: kwakseongjae
# Problem: https://www.acmicpc.net/problem/5639
import sys

# 재귀 제한 완화
sys.setrecursionlimit(10 ** 9)

# 입력 함수 정의
def input():
    return sys.stdin.readline().rstrip()

pre_order = []
while True: 
    # 엔터가 입력될 때 까지 
    try:
        pre_order.append(int(input()))
    except:
        break

def pre_to_post(start, end):
    if start > end:
        return
    mid = end + 1
    for i in range(start + 1, end + 1):
        if pre_order[i] > pre_order[start]:
            mid = i
            break
    pre_to_post(start + 1, mid - 1)  # 왼쪽 트리
    pre_to_post(mid, end)  # 오른쪽 트리
    print(pre_to_post[start])  # 루트 노드 출력

pre_to_post(0, len(pre_order) - 1)