# Authored by: kwakseongjae
# Problem: https://www.acmicpc.net/problem/13164
import sys

def input():
    return sys.stdin.readline().rstrip()

n, k = map(int, input().split())
_list = list(map(int, input().split()))

sub = sorted(_list[i + 1] - _list[i]  for i in range(n-1))

print(sub(sub[:(n-k)]))