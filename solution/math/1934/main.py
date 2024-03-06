# Authored by : kwakseongjae
# Problem: https://www.acmicpc.net/problem/1934
# Reference: https://lifeofyoori.tistory.com/75

T = int(input())
for _ in range(T):
    A, B = map(int, input().split())
    result = A*B

    while B>0:
        A,B = B, A%B

    print(result//A) # 최대공약수를 구하고 A, B의 곱을 최대 공약수로 나누면 최소공배수