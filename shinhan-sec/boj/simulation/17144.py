import sys
read = sys.stdin.readline

R, C, T = map(int, read().split())

board = []
air = []  # 공기청정기 위치 [위 청정기 행, 아래 청정기 행]

for r in range(R):
    row = list(map(int, read().split()))
    if row[0] == -1:
        air.append(r)
    board.append(row)

def spread(board):
    new_board = [row[:] for row in board]
    for r in range(R):
        for c in range(C):
            if board[r][c] <= 0:
                continue
            amt = board[r][c] // 5
            cnt = 0
            for dr, dc in [(-1,0),(1,0),(0,-1),(0,1)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < R and 0 <= nc < C and board[nr][nc] != -1:
                    new_board[nr][nc] += amt
                    cnt += 1
            new_board[r][c] -= amt * cnt
    return new_board

def circulate(board):
    top, bot = air[0], air[1]

    # 윗부분 반시계
    # 위로 당기기 (1열, top+1 ~ 1행)
    for r in range(top - 1, 0, -1):
        board[r][0] = board[r-1][0]
    # 왼쪽으로 당기기 (0행)
    for c in range(0, C - 1):
        board[0][c] = board[0][c+1]
    # 아래로 당기기 (C-1열, 0행 ~ top행)
    for r in range(0, top):
        board[r][C-1] = board[r+1][C-1]
    # 오른쪽으로 당기기 (top행, C-1열 ~ 1열)
    for c in range(C - 1, 1, -1):
        board[top][c] = board[top][c-1]
    board[top][1] = 0  # 공기청정기에서 나오는 칸

    # 아랫부분 시계
    # 아래로 당기기 (1열, bot-1 ~ R-2행)
    for r in range(bot + 1, R - 1):
        board[r][0] = board[r+1][0]
    # 왼쪽으로 당기기 (R-1행)
    for c in range(0, C - 1):
        board[R-1][c] = board[R-1][c+1]
    # 위로 당기기 (C-1열, R-1행 ~ bot행)
    for r in range(R - 1, bot, -1):
        board[r][C-1] = board[r-1][C-1]
    # 오른쪽으로 당기기 (bot행, C-1열 ~ 1열)
    for c in range(C - 1, 1, -1):
        board[bot][c] = board[bot][c-1]
    board[bot][1] = 0  # 공기청정기에서 나오는 칸

    return board

for _ in range(T):
    board = spread(board)
    board = circulate(board)

print(sum(sum(row) for row in board) + 2)  # 공기청정기 -1 두 개 보정