import sys

read = sys.stdin.readline

T = int(read().rstrip())

words = list(set([read().rstrip() for _ in range(T)]))


words.sort(key=lambda x: [len(x), x])

print(*words, sep='\n')
