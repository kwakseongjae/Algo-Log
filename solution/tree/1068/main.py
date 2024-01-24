# Author: kwakseongjae  
# Problem: https://www.acmicpc.net/problem/1068
import sys

# 입력 함수 정의
input = sys.stdin.readline

def dfs(v):
    tree[v] = -2 # 지운 노드는 -2로 초기화
    for i in range(n): 
        if v == tree[i]: 
            dfs(i) 
            
n = int(input())
tree = list(map(int, input().split())) # 각 노드의 부모 저장
erase = int(input()) # 지울 노드의 번호

dfs(erase)

answer = 0
for i in range(n):
    if tree[i] != -2 and i not in tree: 
        answer+=1

print(answer)