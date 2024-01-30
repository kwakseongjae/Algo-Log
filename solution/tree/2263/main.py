# Author: kwakseongjae
# Problem: https://www.acmicpc.net/problem/2263
import sys

# 재귀 조건 완화
sys.setrecursionlimit(10**7)

# 입력 함수 정의
def input(): 
    return sys.stdin.readline().rstrip()

n = int(input())
inorder = list(map(int, input().split()))
postorder = list(map(int, input().split()))

node_num = [0] * (n + 1)
for i in range(n):
    node_num[inorder[i]] = i

def preorder(inStart, inEnd, postStart, postEnd):
    if (inStart > inEnd) or (postStart > postEnd):
        return
    
    root = postorder[postEnd]
    
    leftNode = node_num[root] - inStart
    rightNode = inEnd - node_num[root]
    
    print(root, end = " ")
    preorder(inStart, inStart + leftNode - 1, postStart, postStart + leftNode - 1)
    preorder(inEnd - rightNode + 1, inEnd, postEnd - rightNode, postEnd - 1)

preorder(0, n - 1, 0, n - 1)