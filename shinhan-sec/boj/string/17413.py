import sys
from collections import deque

read = sys.stdin.readline

q = deque()

S = read().rstrip()

tmp_word = ''

for word in S:
    if len(tmp_word) == 0:
        tmp_word += word
    else:
        if word == '>':
            q.append(tmp_word + '>')
            tmp_word = ''
        elif word == '<':
            q.append(tmp_word)
            tmp_word = '<'
        else:
            tmp_word += word

if tmp_word:
    q.append(tmp_word)

answer = ''

for item in q:
    if item[0] == '<':
        answer += item
    else:
        words = item.split()
        tmp = ''
        for word in words:
            tmp += word[::-1] + ' '

        answer += tmp.rstrip()
print(answer)