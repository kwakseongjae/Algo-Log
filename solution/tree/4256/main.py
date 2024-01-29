# Author: kwakseongjae
# Problem: https://www.acmicpc.net/problem/4256
import sys

# 재귀 조건 완화 
sys.setrecursionlimit(10**9)

# 입력 함수 정의
def input():
    return sys.stdin.readline().rstrip()

def postorder(root,start,end):
    for i in range(start,end):
        if inorder[i]==preorder[root]:
            postorder(root+1 , start, i) # inorder의 왼쪽 부분
            postorder(root+1+(i-start) , i+1 , end) #inorder의 오른쪽 부분
            answer.append(preorder[root])

T = int(input())
for i in range(T):
    n = int(input())
    preorder = list(map(int, input().split()))
    inorder = list(map(int, input().split()))
    answer = []
    postorder(0, 0, n)

    # 결과 출력
    print(*answer)