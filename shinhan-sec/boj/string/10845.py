import sys
from collections import deque

read = sys.stdin.readline

N = int(read().rstrip())

q = deque()

def push(x):
    q.append(x)

def front():
    return q[0] if q else -1

def back():
    return q[-1] if q else -1

def empty():
    return 1 if not q else 0

def size():
    return len(q)

def pop():
    return q.popleft() if q else -1

commands = {
    'push' : push,
    'front' : front,
    'back' : back,
    'empty': empty,
    'size': size,
    'pop': pop
}

for _ in range(N):
    command_value = read().rstrip().split()

    if len(command_value) == 2:
        command, value = command_value
        commands[command](value)
    else:
        command = command_value[0]
        print(commands[command]())
