# Authored by : kwakseongjae
# Link : https://www.acmicpc.net/problem/4358
import sys

# 입력 함수 정의
def input():
    return sys.stdin.readline().rstrip()

total = 0
trees = {}
while True:
    tree = input()
    if not tree:
        break
    
    total += 1   
    if tree in trees:   
        trees[tree] += 1
    else:
        trees[tree] = 1

# 튜플이 담긴 리스트로 반환
sorted_trees = sorted(trees.items())

# 사전순으로 정렬한 나무의 이름순서대로 백분율을 계산해 출력
for tree, number_of_tree in sorted_trees:
    per = ((number_of_tree / total) * 100)
    print(tree, round(per, 4))
    # print('%s %.4f' %(tree, per))