# Authored by: kwakseongjae
# Problem: https://www.acmicpc.net/problem/11729
# Reference: https://kbwplace.tistory.com/115

N = int(input())

path = []
def hanoi(n, start=1, mid=2, end=3):
    if n==0: return
    hanoi(n-1, start, end, mid)
    path.append((start, end))
    hanoi(n-1, mid, start, end)

hanoi(N)

print(len(path))
for i in range(len(path)):
    print(path[i][0], path[i][1])
