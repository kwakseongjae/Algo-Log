# Authored by: kwakseongjae
# Problem: https://www.acmicpc.net/problem/1931
import sys

def input():
    return sys.stdin.readline().rstrip()

N = int(input())
arr = []
total = 1

for i in range(N):
    a, b = map(int, input().split())
    arr.append((a, b))
    
arr.sort(key = lambda x: (x[1], x[0]))
end_time = arr[0][1]

for i in range(1, N):
    if arr[i][0] >= end_time:
        end_time = arr[i][1]
        total += 1
        
print(total)