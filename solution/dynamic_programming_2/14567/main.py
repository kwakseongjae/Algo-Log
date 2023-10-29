# Authored by: kwakseongjae
# Problem: https://www.acmicpc.net/problem/14567
import sys
from collections import deque

def input():
    return sys.stdin.readline().rstrip()

n, m = map(int, input().split())

learning = {i: [] for i in range(i, n + 1)}
indegree = [0] * (n + 1)
dp = [1] * (n + 1)

for _ in range(m):
    a, b = map(int, input().split())
    learning[a].append(b)
    indegree[b] += 1
    
queue = deque()
for i in range(1, n + 1):
    if indegree[i] == 0:
        queue.append(i)

while queue:
    current = queue.popleft()
    for next in learning[current]:
        indegree[next] -= 1
        if indegree[next] == 0:
            queue.append(next)
            dp[next] = max(dp[next], dp[current] + 1)

print(" ".join(map(str, dp[1:])))
