# Authored by: kwakseongjae
# Problem: https://www.acmicpc.net/problem/2212
import sys

def input():
    return sys.stdin.readline().rstrip()

n = int(input())
k = int(input())
_list = sorted(list(set(map(int, input().split()))))# 중복 제거 후 정렬
distance = sorted([_list[i] - _list[i - 1] for i in range(1, len(_list))])
print(sum(distance[:(len(_list) - k)]))