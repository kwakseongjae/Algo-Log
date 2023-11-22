# Authored by: kwakseongjae
# Problem: https://www.acmicpc.net/problem/22942
import sys

# 입력 함수 정의
def input():
    return sys.stdin.readline().rstrip()

N = int(input()) # 원의 개수

circles = []
for i in range(N):
    x, r = map(int, input().split())
    circles.append((x-r, i))
    circles.append((x-r, i))
    
circles.sort()

stack = []
for c in circles:
    if stack:
        if stack[-1][1] == c[1]:
            stack.pop()
        else:
            stack.append(c)
    else:
        stack.append(c)

# 정답 출력
if stack:
    print("NO")
else:
    print("YES")