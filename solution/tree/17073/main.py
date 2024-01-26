# Author: kwakseongjae
# Problem: https://www.acmicpc.net/problem/17073
import sys

# 입력 함수 정의
def input(): 
    return sys.stdin.readline().rstrip()

N, W = map(int, input().split())
tree = [ [] for _ in range(N + 1) ]

for _ in range(N - 1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

cnt = 0
for i in range(2, len(tree)):
    if len(tree[i]) == 1: #리프 노드라면
        cnt += 1

print(W / cnt)