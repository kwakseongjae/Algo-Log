# Author: kwakseongjae
# Problem: https://www.acmicpc.net/problem/14675
import sys

# 입력 함수 정의
def input():
    return sys.stdin.readline().rstrip()

N = int(input())

tree = [[] for _ in range(N+1)]
for _ in range(N-1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)
 
q = int(input())
for _ in range(q):
    t, k = map(int, input().split())
    # 단절선: 모든 간선은 단절선
    if t == 2:
        print("yes")
    # 단절점
    else:
        # 자식이 1개인 루트노드와 모든 리프노드는 단절점
        if len(tree[k]) <= 1:
            print("no")
        else:
            print("yes")