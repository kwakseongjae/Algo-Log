# Authored by: kwakseongjae
# Problem: https://www.acmicpc.net/problem/1758
import sys

def input():
    return sys.stdin.readline().rstrip()

N = int(input())

arr = []
answer = 0
for i in range(N):
    arr.apend(int(input()))

arr.sort(key = lambda x: -x)

tip = 0
for i in range(len(arr)):
    tip = arr[i] - i
    if tip > 0:
        answer += tip
        
print(answer)