# Authored by : kwakseongjae
# Link : http://boj.kr/c5acf6a6a2f24b4ca0c415fbe1947571
import sys
import heapq

# 입력 함수 정의
def input():
    return sys.input()


def check(data):
    left, right = [], []
    middle = data[0]
    result = [middle]
    for idx, value in enumerate(data[1:], 1):
        if value > middle:
            heapq.heappush(right, value)
        else:
            heapq.heappush(left, -value)
            
        if idx % 2 == 0:
            if len(left) < len(right):
                heapq.heappush(left, -middle)
                middle = heapq.heappop(right)
            elif len(left) > len(right):
                heapq.heappush(right, middle)
                middle = -heapq.heappop(left)
            result.append(middle)

    length = len(result)
    print(length)
    for i in range(length):
        if (i + 1) != 1 and (i + 1) % 10 == 1:
            print()
        print(result[i], end=' ')
    print()


T = int(input())
for _ in range(T):
    m = int(input())
    
    data = []
    if m % 10 == 0:
        for _ in range(m // 10):
            data.extend(list(map(int, input().split())))
    else:
        for _ in range(m // 10 + 1):
            data.extend(list(map(int, input().split())))

    check(data)