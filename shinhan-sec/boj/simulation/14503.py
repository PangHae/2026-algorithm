import sys

# 0 - 북 1 - 동 2 - 남 3 - 서

read = sys.stdin.readline

N, M = map(int, read().rstrip().split())

start_x, start_y, start_dir = map(int, read().rstrip().split())

def get_back_dir(cur_dir):
    match cur_dir:
        case 0:
            return 2
        case 1:
            return 3
        case 2:
            return 0
        case 3:
            return 1

board = []
is_cleaned = [[False for _ in range(M)] for _ in range(N)]

for _ in range(N):
    row = list(map(int, read().rstrip().split()))
    board.append(row)

cur_x = start_x
cur_y = start_y
cur_dir = start_dir

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

while True:
    if not is_cleaned[cur_x][cur_y]:
        is_cleaned[cur_x][cur_y] = True

    near_is_all_cleaned = True

    for i in range(4):
        nx = cur_x + dx[i]
        ny = cur_y + dy[i]

        if 0 <= nx < N and 0 <= ny < M and board[nx][ny] == 0 and not is_cleaned[nx][ny]:
            near_is_all_cleaned = False
            break

    if near_is_all_cleaned:
        backward = get_back_dir(cur_dir)
        nx = cur_x + dx[backward]
        ny = cur_y + dy[backward]

        if board[nx][ny] == 1:
            break
        else:
            cur_x = nx
            cur_y = ny
    else:
        cur_dir = cur_dir - 1 if cur_dir - 1 >= 0 else 3

        nx = cur_x + dx[cur_dir]
        ny = cur_y + dy[cur_dir]

        if board[nx][ny] == 0 and not is_cleaned[nx][ny]:
            cur_x = nx
            cur_y = ny

answer = 0

for i in range(N):
    for j in range(M):
        if is_cleaned[i][j]:
            answer += 1

print(answer)