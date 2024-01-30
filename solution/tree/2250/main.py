# Author: kwakseongjae
# Problem: https://www.acmicpc.net/problem/2250
import sys

# 재귀 조건 완화
sys.setrecursionlimit(10**6)

# 입력 함수 정의
def input(): 
    return sys.stdin.readline().rstrip()

 
class Node:
    def __init__(self):
        self.left = -1
        self.right = -1
        self.depth = 0
        self.order = 0
 
def inorder(node, depth):
    global order
    if node == -1:
        return
    inorder(a[node].left, depth+1)
    a[node].depth = depth
    order += 1
    a[node].order = order
    inorder(a[node].right, depth+1)
 
N = int(input())
a = [Node() for _ in range(N+1)]
left = [0]*10001
right = [0]*10001
parent = [0]*10001
order = 0
 
for _ in range(N):
    nd_num, left_node, right_node = map(int, input().split())
    a[nd_num].left = left_node
    a[nd_num].right = right_node
    if left_node != -1:
        parent[left_node]+=1
    if right_node != -1:
        parent[right_node]+=1
 
 
root = 0
for i in range(1, N+1):
    if parent[i] == 0:
        root = i
 
inorder(root, 1)

max_depth = 0
for i in range(1, N+1):
    depth = a[i].depth
    order = a[i].order
    if left[depth] == 0:
        left[depth] = order
    else:
        left[depth] = min(left[depth], order)
        
    right[depth] = max(right[depth], order)
    max_depth = max(max_depth, depth)

widthest_level = 0 
max_width = 0
for i in range(1, max_depth+1):
    if max_width < right[i] - left[i] + 1:
        max_width = right[i]-left[i]+1
        widthest_level = i
 
print(widthest_level, max_width)