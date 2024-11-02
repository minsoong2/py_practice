import sys

size = int(sys.stdin.readline())
move_list = list(map(str, sys.stdin.readline().split()))
r, c = 1, 1
for move in move_list:
    if move == 'R':
        c += 1
        if c > size:
            c -= 1
    elif move == 'L':
        c -= 1
        if c < 1:
            c += 1
    elif move == 'U':
        r -= 1
        if r < 1:
            r += 1
    elif move == 'D':
        r += 1
        if r > size:
            r -= 1
    else:
        pass

print(r, c)