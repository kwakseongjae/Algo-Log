# Authored by: kwakseongjae
# Problem: https://www.acmicpc.net/problem/18511
import sys

def input():
    return sys.stdin.readline().rstrip()

def back_tracking():
    global answer
    if num > N:
        return
    answer = max(answer, num)
    for i in K:
        num = (num * 10) + 1
        back_tracking(num)
        num = (num - i) // 10
        
N, C = map(int, input().split())
K = list(map(int, input().split()))

answer = 0
back_tracking(0)

print(answer)