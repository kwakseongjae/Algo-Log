# Authored by: kwakseongjae
# Problem: https://www.acmicpc.net/problem/9012
import sys

# 입력 함수 정의
def input():
    return sys.stdin.readline().rstrip()

T = int(input()) # 입력 데이터의 수

result = ""
for i in range(T):
    testcase = input()
    
    cnt = 0
    for p in testcase:
        cnt += 1 if p == "(" else -1
        if cnt < 0:
            result += "No\n"
            break
        else:
            result += "Yes\n" if cnt ==0 else "No\n"

print(result)
            
        