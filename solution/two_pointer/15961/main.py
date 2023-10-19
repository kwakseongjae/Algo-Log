# Authored by: kwakseongjae
# Problem: https://www.acmicpc.net/problem/15961
import sys

def input():
    return sys.stdin.readline().rstrip()

n, f_kind, max_seq, coupon = map(int, input().split())
line = [int(input()) for _ in range(n)]

def answer(line, max_seq, coupon):
    cnt = 0
    eat = [0 for _ in range(3000001)]
    for i in range(max_seq):
        food_num = line[i]
        if not eat[food_num]:
            cnt += 1
        eat[food_num] += 1

    max_cnt = cnt
    for i in range(1, n):
        if max_cnt <= cnt:
            if not eat[coupon]:
                max_cnt = cnt + 1
            else:
                max_cnt = cnt
                
        out = i - 1
        eat[line[out]] -= 1
        if not eat[line[out]]:
            cnt -= 1
        
        in_ = (i + max_seq - 1) % n
        if not eat[line[in_]]:
            cnt += 1
        eat[line[in_]] += 1
    
    return max_cnt

print(answer(line, max_seq, coupon))