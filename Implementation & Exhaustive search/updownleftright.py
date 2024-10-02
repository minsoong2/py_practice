import sys

size = int(sys.stdin.readline())
move_list = list(map(str, sys.stdin.readline().split()))
matrix_udlr = [1, 1]
cnt = 0

for move in move_list:
    if move == 'U':
        matrix_udlr[0] -= 1
        if matrix_udlr[0] == 0:
            matrix_udlr[0] = 1
        cnt += 1
    elif move == 'D':
        matrix_udlr[0] += 1
        if matrix_udlr[0] == size + 1:
            matrix_udlr[0] = size
        cnt += 1
    elif move == 'L':
        matrix_udlr[1] -= 1
        if matrix_udlr[1] == 0:
            matrix_udlr[1] = 1
        cnt += 1
    elif move == 'R':
        matrix_udlr[1] += 1
        if matrix_udlr[1] == size + 1:
            matrix_udlr[1] = size
        cnt += 1
    else:
        pass

print(matrix_udlr[0], matrix_udlr[1])

# for i in range(1, size+1):
#     for j in range(1, size+1):
#         matrix_udlr.append((i, j))

