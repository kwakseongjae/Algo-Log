# Author: kwakseongjae
# Problem: https://www.acmicpc.net/problem/20924
import sys

# 재귀 조건 완화
sys.setrecursionlimit(10**7)

# 입력 함수 정의
def input():
    return sys.stdin.readline().rstrip()

N, R = map(int, input().split())
tree = [[] for _ in range(N + 1)]

for _ in range(N-1):
    a, b, d = map(int,input().rstrip().split())
    tree[a].append((b, d))
    tree[b].append((a, d))


answer =[0, 0]
def dfs(child, parent, sum, flag):
    # 기가 노드까지의 간선 길이의 합
    if flag == 0:  
        answer[0] = sum 
    # 긴 가지의 길이
    else: 
        answer[1] = max(answer[1], sum) 
    # flag를 통해서 0이면 기가 노드 까지의 간선 길이의 합을 구해주고, 
    # 1이면 리프노드를 돌면서 가장 긴 가지의 길이를 구한다.    
    if (flag == 0) and (len(tree[child]) > 2 -int(child == R)): 
        flag, sum = 1, 0
        
    for node, dist in tree[child]:
        if node == parent: 
            continue
        dfs(node, parent, sum+dist, flag)

# answer 초기화
dfs(R, R, 0, 0)

# 결과 출력
print(answer[0], answer[1])