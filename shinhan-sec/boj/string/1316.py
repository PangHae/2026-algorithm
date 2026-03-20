import sys
from collections import defaultdict

read = sys.stdin.readline

N = int(read().rstrip())

answer = 0

for _ in range(N):
    word = read().rstrip()
    before_a = ''
    word_dict = defaultdict(int)
    is_group_word = True

    for a in word:
        if a in word_dict:
            if before_a != a:
                is_group_word = False
                break
            else:
                before_a = a
                continue
        else:
            word_dict[a] = 1
            before_a = a

    if is_group_word:
        answer += 1

print(answer)
