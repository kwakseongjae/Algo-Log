# Authored by: kwakseongjae
# Problem: https://www.acmicpc.net/problem/5568
import sys
from itertools import permutations

def input():
    return sys.stdin.readline().rstrip()

n = int(input())
k = int(input())

arr = []
for i in range(n):
    arr.append(input())

per = list(permutations(arr, k))
answer = set()
for i in range(len(per)):
    str = ""
    for j in range(len(per[i])):
        str += per[i][j]
    answer.add(str)

answer = list(answer)
print(len(answer))
    

