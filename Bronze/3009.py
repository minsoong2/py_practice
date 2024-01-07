x = []
y = []
for i in range(3):
    a, b = map(int, input().split())
    x.append(a)
    y.append(b)

re_x, re_y = 0, 0
for i in range(3):
    x_cnt = x.count(x[i])
    y_cnt = y.count(y[i])
    if x_cnt == 1:
        re_x = x[i]
    if y_cnt == 1:
        re_y = y[i]

print(re_x, re_y)