# Authored by: kwakseongjae
# Problem: https://www.acmicpc.net/problem/1969
import sys

def input():
    return sys.stdin.readline().rstrip()

N, M = map(int, input().split())

arr = []
word = ""
dist = 0

for _ in range(N):
    arr.append(input())
    
for i in range(M):
    dict = {}
    for j in range(N):
        if arr[j][i] not in dict:
            dict[arr[j][i]] = 1
        else:
            dict[arr[j][i]] += 1

    answer = list(dict.items())
    answer.sort(key = lambda x: (-x[1], x[0]))
    word += answer[0][0]
    dist += N - answer[0][1]

print(word)
print(dist)