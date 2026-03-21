import sys

read = sys.stdin.readline

N, W = map(int, read().rstrip().split())

bags = [list(map(int, read().rstrip().split())) for _ in range(N)]

dp = [[0 for _ in range(len(bags))] for _ in range(W + 1)]

for i in range(1, W+1):
    for j in range(N):
        w, v = bags[j]
        if j == 0:
            dp[i][j] = v if w<= i else 0
        elif w > i:
            dp[i][j] = dp[i][j-1]
        else:
            dp[i][j] = max(dp[i][j-1], dp[i-w][j-1] + v)

print(dp[W][N-1])