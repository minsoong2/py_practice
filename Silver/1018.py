board1 = [['' for j in range(8)] for i in range(8)]
board2 = [['' for j in range(8)] for i in range(8)]
for i in range(8):
    for j in range(8):
        if (j % 2 == 0 and i % 2 == 0) or (j % 2 != 0 and i % 2 != 0):
            board1[i][j], board2[i][j] = 'W', 'B'
        else:
            board1[i][j], board2[i][j] = 'B', 'W'

a, b = map(int, input().split())
matrix = []
for i in range(a):
    s = list(input())
    if len(s) == b:
        matrix.append(s)

cnt_1 = [[0 for j in range(b-7)] for i in range(a-7)]
cnt_2 = [[0 for j in range(b-7)] for i in range(a-7)]
min_list = []
for i in range(a-7):
    for j in range(b-7):
        for k in range(len(board1)):
            for l in range(len(board1[0])):
                if board1[k][l] == matrix[i + k][j + l]:
                    pass
                else:
                    cnt_1[i][j] += 1

for i in range(a-7):
    m = min(cnt_1[i])
    min_list.append(m)

for i in range(a-7):
    for j in range(b-7):
        for k in range(len(board2)):
            for l in range(len(board2[0])):
                if board2[k][l] == matrix[i + k][j + l]:
                    pass
                else:
                    cnt_2[i][j] += 1

for i in range(a-7):
    m = min(cnt_2[i])
    min_list.append(m)

print(min(min_list))