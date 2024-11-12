import sys

def draw_star(n):
    if n == 1:
        return '*'
    star = draw_star(n // 3)

    stars = []
    for i in star:
        stars.append(i * 3)
    for j in star:
        stars.append(j + ' ' * (n//3) + j)
    for k in star:
        stars.append(k * 3)

    return stars

n = int(sys.stdin.readline())
for draw in draw_star(n):
    print(draw)