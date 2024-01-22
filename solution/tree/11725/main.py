# Authored by : kwakseongjae
# Problem: https://www.acmicpc.net/problem/11725
import sys

# 재귀 제한 완화
sys.setrecursionlimit(10**6)

# 입력 함수 정의
def input():
    return sys.stdin.readline().rstrip()


n = int(input())

# 부모 노드 저장 리스트
parent = [0] * (n+1)

# 양방향 연결 정보 저장 리스트
graph = [[] for _ in range(n+1)]

for _ in range(n-1):
    # 양방향 연결 정보 입력 및 저장
    start, end = map(int, input().split())
    graph[start].append(end)
    graph[end].append(start)

# 부모 노드 탐색
def dfs(root):
    # 현재 노드와 연결된 노드 확인
    for neighbor in graph[root]:
        # 연결된 노드의 부모가 없다면
        if (parent[neighbor] == 0):
            parent[neighbor] = root
            dfs(neighbor)

# 1번 노드부터 탐색 시작
dfs(1)

# 결과 출력
for i in range(2, n+1):
    print(parent[i])