import sys

read = sys.stdin.readline

N = int(read().rstrip())

count = 0
answer = []

for _ in range(N):
    word = read().rstrip()
    reverse_word = word[::-1]
    half_len = len(word) // 2

    is_pelindrom = True

    for i in range(half_len):
        if word[i] != reverse_word[i]:
            is_pelindrom = False
            break
    if is_pelindrom:
        count += 1
        answer.append(word)

answer.sort(key= lambda x: (-len(x), x))

print(count)
print(answer[0]) if count != 0 else print('NONE')