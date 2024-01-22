# Authored by : kwakseongjae
# Problem: https://www.acmicpc.net/problem/1991

import sys

# 입력 함수 정의
def input():
    return sys.stdin.readline().rstrip()

n = int(input())
tree = {}
for i in range(n):
    root, left, right = map(str, input().split())  # 루트, 왼쪽자식, 오른쪽 자식
    tree[root] = left, right  # {'A': ('B', 'C')}

# 전위 순회 함수 정의
def preorder(v):  
    if v != ".": 
        print(v, end="")
        preorder(tree[v][0])  
        preorder(tree[v][1])  

# 중위 순회 함수 정의
def inorder(v):  
    if v != ".":  
        inorder(tree[v][0])  
        print(v, end="")  
        inorder(tree[v][1])  

# 후위 순위 함수 정의
def postorder(v):  
    if v != ".":  
        postorder(tree[v][0])  
        postorder(tree[v][1])  
        print(v, end="")  

#루트노드 'A'
preorder('A')
print()
inorder('A')
print()
postorder('A')