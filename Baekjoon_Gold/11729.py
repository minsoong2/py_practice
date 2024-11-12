import sys

n = int(sys.stdin.readline())
cnt = 0
re = []

def move(start, to):
    global cnt, re
    cnt += 1
    re.append((start, to))

def hanoi(N, start, to, via):
    if N == 1:
        move(start, to)
    else:
        hanoi(N-1, start, via, to)
        move(start, to)
        hanoi(N-1, via, to, start)

hanoi(n, 1, 3, 2)

print(cnt)
for tup in re:
    start, end = tup[0], tup[1]
    print(start, end)