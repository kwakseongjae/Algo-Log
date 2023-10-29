# Authored by: kwakseongjae
# Problem: https://www.acmicpc.net/problem/11399
import sys

def input():
    return sys.stdin.readline().rstrip()

N = int(input())
arr = list(map(int, input().split())) 
arr. sort()

total = 0
waiting = 0
for i in range(len(arr)):
    total += arr[i] + waiting
    waiting += arr[i]

print(total)          