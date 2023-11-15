# Authored by: kwakseongjae
# Problem: https://www.acmicpc.net/problem/2141
import sys

def input():
    return sys.stdin.readline().rstrip()

n = int(input())
_list = [list(map(int, input().split())) for i in range(n)]
_list.sort()

dist = 0
r_man, l_man = 0, 0
for i in range(n):
    tmp = _list[i][0] - _list[0][0]
    dist += tmp * _list[i][1]
    r_man += _list[i][1]
    
min_dist = dist
sol = _list[0][0]
for i in range(1, n):
    tmp = _list[i][0] - _list[i - 1][0]
    l_man += _list[i - 1][1]
    r_man -= _list[i - 1][1]
    dist += (l_man - r_man) * tmp
    
    if min_dist > dist:
        min_dist = dist
        sol = _list[i][0]
        
print(sol)