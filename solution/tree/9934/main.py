# Author: kwakseongjae
# Problem: https://www.acmicpc.net/problem/9934
import sys

# 입력 함수 정의
def input():
    return sys.stdin.readline().rstrip()

K = int(input())
entry_order = list(map(int, input().split()))

answer = [[] for _ in range(K)]
def dfs(entry_order, depth):
    # 트리의 root index를 찾아낸다.
    mid = (len(entry_order) // 2)
    answer[depth].append(entry_order[mid])
    if len(entry_order) == 1:
        return

    dfs(entry_order[: mid], depth + 1)
    dfs(entry_order[mid+1:], depth + 1)

# answer 초기화
dfs(entry_order, 0)

# 결과 출력 
for i in answer:
    print(*i)