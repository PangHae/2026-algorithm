import sys
from collections import deque

read = sys.stdin.readline

comp = list(read().rstrip())

stack = deque()

ops = {'+' : 1, '-' : 1, '*' : 2, '/' : 2}

answer = ''

for token in comp:
    if token == '(':
        stack.append(token)
    elif token == ')':
        while stack and stack[-1] != '(':
            answer+=stack.pop()
        stack.pop()
    elif token in ops:
        while stack and stack[-1] != '(' and ops[stack[-1]] >= ops[token]:
            answer += stack.pop()
        stack.append(token)
    else:
        answer += token

while stack:
    answer += stack.pop()

print(answer)