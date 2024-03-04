# Author: Kwakseonjae
# Problem: https://www.acmicpc.net/problem/2343
# Reference: https://codingwonny.tistory.com/311

N, M = map(int, input().split())
time_list = list(map(int, input().split()))

start = max(time_list)
end = sum(time_list)
answer = 0
while start <= end:
    mid = (start + end) // 2 

    total = 0
    cnt = 1
    for time in time_list:
        if total + time > mid:
            cnt += 1
            total = 0
        total += time 

    if cnt <= M:
        answer = mid
        end = mid - 1
    else:
        start = mid + 1
    
print(answer)