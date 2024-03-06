# Authored by: kwakseongjae
# Problem: https://www.acmicpc.net/problem/11653
# Reference: https://codinghani.tistory.com/5

N = int(input())

if N == 1:
    print('')

# 2부터 하나씩 나눠보기
for num in range(2, N+1):
    if N % num == 0:
    	#해당 숫자로 나눌 수 없을 때까지 나누기
        while N % num == 0:
            print(num)
            N = N // num