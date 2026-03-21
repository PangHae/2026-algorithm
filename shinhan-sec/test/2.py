import sys
from collections import deque

read = sys.stdin.readline

N, M = map(int, read().rstrip().split())
board = [list(map(int, read().rstrip())) for _ in range(N)]

visited = [[[False, False] for _ in range(M)] for _ in range(N)]
visited[0][0][0] = True

q = deque()
q.append((0, 0, 1, False))

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

answer = -1

while q:
    x, y, count, used = q.popleft()

    if x == N - 1 and y == M - 1:
        answer = count
        break

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < N and 0 <= ny < M:
            used_int = 1 if used else 0

            if board[nx][ny] == 0 and not visited[nx][ny][used_int]:
                visited[nx][ny][used_int] = True
                q.append((nx, ny, count + 1, used))
            if board[nx][ny] == 1 and not used and not visited[nx][ny][1]:
                visited[nx][ny][1] = True
                q.append((nx, ny, count + 1, True))

print(answer)