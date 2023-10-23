# Authored by: kwakseongjae
# Problem: https://www.acmicpc.net/problem/9012
import sys

def input():
    return sys.stdin.readline().rstrip()

N = int(input())

result = ""
for i in range(N):
    testcase = input()
    cnt = 0
    for p in testcase:
        cnt += 1 if p == "(" else -1
        if cnt < 0:
            result += "No\n"
            break
        else:
            result += "Yes\n" if cnt ==0 else "No\n"

print(result)
            
        