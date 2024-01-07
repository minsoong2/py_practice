num = int(input())
x = []
y = []
for i in range(num):
    a, b = map(int, input().split())
    x.append(a)
    y.append(b)

x_max, x_min, y_max, y_min = max(x), min(x), max(y), min(y)

print((x_max - x_min) * (y_max - y_min))