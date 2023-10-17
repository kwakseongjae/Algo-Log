# Authored by: kwakseongjae
# Problem : https://www.acmicpc.net/problem/14916
import sys

def input():
    return sys.stdin.readline().rstrip()

N = int(input())

answer = 0
if N < 5:
    if N % 2 != 0:
        answer = -1
    else:
        answer = N // 2
else:
    cnt, N = divmod(N, 5)
    if N == 0:
        answer = cnt
    else:
        if N % 2 == 0:
            cnt += N // 2
            answer = cnt
        else:
            cnt += ((N + 5) // 2) - 1
            answer = cnt

print(answer)
        