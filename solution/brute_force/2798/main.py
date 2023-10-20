# Authored by: kwakseongjae
# Problem: https://www.acmicpc.net/problem/11286
import sys

def input():
    return sys.stdin.readline().rstrip()

N, M = map(int, input().split())
arr = list(map(int, input().split()))

MAX = 0
for i in range(len(arr)):
    for j in range(i+1, len(arr)):
        for k in range(len(j+1, arr)):
            if arr[i] + arr[j] + arr[k] <= M:
                MAX = max(MAX, arr[i] + arr[j] + arr[k])  
                
print(MAX)          