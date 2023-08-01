a, b = map(int, input().split())

matrix_1, matrix_2 = [], []
for i in range(a):
    row = list(map(int, input().split()))
    matrix_1.append(row)

for i in range(a):
    row = list(map(int, input().split()))
    matrix_2.append(row)

for i in range(a):
    for j in range(b):
        print(matrix_1[i][j] + matrix_2[i][j], end=' ')
    print()