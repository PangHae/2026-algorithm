import sys
from collections import deque

read = sys.stdin.readline

N = int(read().rstrip())

board = [[0 for _ in range(N)] for _ in range(N)]

K = int(read().rstrip())
for _ in range(K):
    x, y = map(int, read().rstrip().split())
    board[x-1][y-1] = 1

board[0][0] = 2

dir_switch = deque()
L = int(read().rstrip())
for _ in range(L):
    time, direction = read().rstrip().split()
    dir_switch.append([int(time), direction])

def change_dir(code, change_pos):
    match code:
        case 'L':
            return change_pos - 1 if change_pos - 1 >= 0 else 3
        case 'D':
            return change_pos + 1 if change_pos + 1 < 4 else 0

cur_time = 0
head_pos = [0, 0]
tail_pos = [0, 0]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
head_dir = 1
tail_dir = 1
head_switched_pos = deque()

while True:
    if dir_switch and dir_switch[0][0] == cur_time:
        head_dir = change_dir(dir_switch[0][1], head_dir)
        _, direction = dir_switch.popleft()
        head_switched_pos.append([[head_pos[0], head_pos[1]], direction])

    head_nx = head_pos[0] + dx[head_dir]
    head_ny = head_pos[1] + dy[head_dir]
    tail_nx = tail_pos[0] + dx[tail_dir]
    tail_ny = tail_pos[1] + dy[tail_dir]

    if 0 <= head_nx < N and 0 <= head_ny < N:
        if board[head_nx][head_ny] == 2:
            cur_time += 1
            break
        elif board[head_nx][head_ny] == 1:
            head_pos[0] = head_nx
            head_pos[1] = head_ny
            board[head_nx][head_ny] = 2
        else:
            if head_switched_pos and tail_pos[0] == head_switched_pos[0][0][0] and tail_pos[1] == head_switched_pos[0][0][1]:
                tail_dir = change_dir(head_switched_pos[0][1], tail_dir)
                head_switched_pos.popleft()
                tail_nx = tail_pos[0] + dx[tail_dir]
                tail_ny = tail_pos[1] + dy[tail_dir]

            board[head_nx][head_ny] = 2
            board[tail_pos[0]][tail_pos[1]] = 0
            head_pos[0] = head_nx
            head_pos[1] = head_ny
            tail_pos[0] = tail_nx
            tail_pos[1] = tail_ny
        cur_time += 1
    else:
        cur_time += 1
        break

print(cur_time)