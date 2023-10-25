# Authored by: kwakseongjae
# Problem: https://www.acmicpc.net/problem/1806
import sys

def input():
    return sys.stdin.readline().rstrip()

n, s = map(int, input().split())
num_list = list(map(int, input().split()))

l_p, r_p, cur_sum, min_len = 0, 0, 0, 100002
# cur_su에 저장되는 구간합: sum(num_list[l_p: r_p])

while l_p < n:
    if cur_sum >= s: # 현재 구간이 주어진 s보다 크다면
        min_len = min(min_len, r_p - l_p) # 현재 구간 길이(r_p - l_p)가 최소라면 업데이트
        cur_sum -= num_list[l_p] # 왼쪽 포인터를 한 칸 오른쪽으로 옮기고 구간합 업데이트
        l_p += 1
    elif r_p == n: # 오른쪽 포인터가 끝에 도달한 경우
        break
    else:
        cur_sum += num_list[r_p] # 오른쪽 구간을 움직여서 구간합 업데이트
        r_p += 1
        
print(min_len if min_len < 100001 else 0)