# Authored by: kwakseongjae
# Problem: https://www.acmicpc.net/problem/5597
import sys

def input():
    return sys.stdin.readline().rstrip()

numbers = [False for _ in range(31)]

for _ in range(28):
    n = int(input())
    numbers[n] = True

answer = []

for i in range(1, 31):
    if not numbers[i]:
        answer.append(i)

print(answer[0])
print(answer[1])