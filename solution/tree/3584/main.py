# Author: kwakseongjae
# Problem: https://www.acmicpc.net/problem/3584
import sys

def input():
    return sys.stdin.readline().rstrip()

def find_parent(parent, x):
    result = [x]
    while parent[x]:
        result.append(parent[x])
        x = parent[x]
    return result

T = int(input())
for _ in range(T):
    N = int(input())
    parent = [0 for _ in range(N + 1)]
    for _ in range(N-1):
        a, b = map(int, input().split())
        parent[b] = a

    x, y = map(int, input().split())
    
    # 각 부모 리스트 정의
    x_parent = find_parent(parent, x)
    y_parent = find_parent(parent, y)

    # 두 노드의 레벨을 맞춘다.
    i, j = 0, 0
    if len(x_parent) > len(y_parent):
        i = len(x_parent) - len(y_parent)
    else:
        j = len(y_parent) - len(x_parent)

    # 같은 깊이에서 최소 공통 조상 찾기: LCA
    while x_parent[i] != y_parent[j]:
        i += 1
        j += 1
        
    # 결과 출력
    print(x_parent[i])