import sys
from collections import deque

read = sys.stdin.readline

T = int(read().rstrip())

for _ in range(T):
    words = list(read().rstrip())
    stack = deque()
    flag = False

    for word in words:
        if word == '(':
            stack.append('(')
        else:
            if not stack:
                print('NO')
                flag = True
                break
            else:
                stack.pop()

    if not flag:
        if not stack:
            print('YES')
        else:
            print('NO')

