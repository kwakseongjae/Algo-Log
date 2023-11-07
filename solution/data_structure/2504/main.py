# Authored by: kwakseongjae
# Problem: https://www.acmicpc.net/problem/2504
import sys

def input():
    return sys.stdin.readline().rstrip()

str = input()
stack = []

# Check Breacket
for ch in str:
    if ch == "(":
        stack.append("(")
    elif ch == "[":
        stack.append("]")
    elif ch == ")":
        if stack and stack[-1] == "(":
            stack.pop(-1)
        else:
            print(0)
            exit(0)
    else:
        if stack and stack[-1] == "[":
            stack.pop(-1)
        else:
            print(0)
            exit(0)
            
if stack:
    print(0)
    exit(0)
    
# compress (add) Integers
def compress():
    while len(stack) > 1:
        a, integer1 = stack[-1]
        b, integer2 = stack[-2]
        if a or b:
            break
        stack.pop()
        stack.pop()
        stack.append((None, integer1 + integer2))

for ch in str:
    if ch == "(":
        stack.append(("(", 2))
    elif ch == "[":
        stack.append(("[", 3))
    elif ch == ")" or ch == "]":
        last1, last2 = stack.pop()
        if last1 != None:
            stack.append((None, last2))
        else:
            a, b = stack.pop()
            stack.append((None, last2 * b))
        compress()
        
print(stack[-1][1])