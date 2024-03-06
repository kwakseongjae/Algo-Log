# Authored by: kwakseongjae
# Problem: https://www.acmicpc.net/problem/1439
# Reference: https://velog.io/@yj_lee/%EB%B0%B1%EC%A4%80-1439%EB%B2%88-%EB%92%A4%EC%A7%91%EA%B8%B0-%ED%8C%8C%EC%9D%B4%EC%8D%AC

S = input()

cnt = 0
prev = S[0]
for i in S[1:]:
    if i != prev: cnt += 1
    
    prev = i


print((cnt + 1) // 2)
