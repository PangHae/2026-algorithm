import sys

read = sys.stdin.readline

# 0: →, 1: ↑, 2: ←, 3: ↓
dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

def get_dirs(start_dir, gen):
    dirs = [start_dir]
    for _ in range(gen):
        # 핵심: 역순으로 뒤집고 +1 (mod 4)
        new_dirs = [(d + 1) % 4 for d in reversed(dirs)]
        dirs += new_dirs
    return dirs

def solve():
    visited = [[False]*101 for _ in range(101)]

    N = int(read().rstrip())
    for _ in range(N):
        x, y, d, g = map(int, read().rstrip().split())
        dirs = get_dirs(d, g)

        visited[x][y] = True
        cx, cy = x, y
        for direction in dirs:
            cx += dx[direction]
            cy += dy[direction]
            visited[cx][cy] = True

    ans = 0
    for x in range(100):
        for y in range(100):
            if (visited[x][y] and visited[x+1][y] and
                visited[x][y+1] and visited[x+1][y+1]):
                ans += 1
    print(ans)

solve()