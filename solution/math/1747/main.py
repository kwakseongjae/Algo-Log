# Authored by: kwakseongjae
# Problem: https://www.acmicpc.net/problem/1747
# Reference: https://develop247.tistory.com/217

def isPrime(x):
    if x == 1:
        return False
    for i in range(2, int(x**0.5)+1):
        if x % i == 0:
            return False
    return True

def isPalindrome(x):
    if str(x) == str(x)[::-1]:
        return True
    return False

N = int(input())
while True:
    if isPalindrome(N) and isPrime(N):
        print(N)
        break
    N += 1