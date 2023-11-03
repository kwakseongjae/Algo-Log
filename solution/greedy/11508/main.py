# Authored by: kwakseongjae
# Proble: https://www.acmicpc.net/problem/11508
import sys

def input():
    return sys.stdin.readline().rstrip()

N = int(input())

arr = []
total = 0
for i in range(N):
    arr.append(int(input()))
    
arr.sort(reverser = True)

ct = 1
for i in range(N):
    if ct % 3 == 0:
        ct = 1
        continue
    
    total += arr[i]
    ct += 1

print(total)