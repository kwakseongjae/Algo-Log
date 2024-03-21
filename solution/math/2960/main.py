# Authored by: kwakseongjae
# Problem: https://www.acmicpc.net/problem/2960
# Reference: https://somjang.tistory.com/entry/BaeKJoon-2960%EB%B2%88-%EC%97%90%EB%9D%BC%ED%86%A0%EC%8A%A4%ED%85%8C%EB%84%A4%EC%8A%A4%EC%9D%98-%EC%B2%B4-%EB%AC%B8%EC%A0%9C-%ED%92%80%EC%9D%B4

N, K = map(int, input().split())

nums = [True] * (N + 1)
cnt = 0
for i in range(2, N+2):
    for j in range(i, N+1, i):
        if nums[j] == True:
            nums[j] = False
            cnt += 1
            if cnt == K:
                print(j)
                break