# Authored by: kwakseongjae 
# Problem: https://www.acmicpc.net/problem/2800
import sys

def input():
    return sys.stdin.readline().rstrip()

s = input()
N = len(s)

index = [ -1 for _ in range(N)]
stack = []
current_idx = 0

for idx, ch in enumerate(s):
    if ch == "(":
        stack.append(current_idx)
        index[idx] = current_idx
        current_idx += 1
    elif ch == ")":
        index[idx] = stack.pop()
        
answer = []
choose = [0 for _ in range(current_idx)]

def func(cnt):
    if cnt == current_idx:
        erase_bracket_cnt = sum(choose)
        if erase_bracket_cnt == 0:
            return
        
        str = ""
        for idx, ch in enumerate(s):
            if index[idx] == -1 or choose[index[idx]] == 0:
                str += ch
        
        answer.append(str)
        return
    
    choose[cnt] = 1
    func(cnt + 1)
    choose[cnt] = 0
    func(cnt + 1)

# Run
func(0)

# 중복 제거
answer = sorted(set(answer))
print("\n".join(answer))
