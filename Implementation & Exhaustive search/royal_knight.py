import sys

xy = sys.stdin.readline()
move = [(2, 1), (2, -1), (-2, 1), (-2, -1),
        (1, 2), (1, -2), (-1, 2), (-1, -2)]

x = ord(xy[0]) - ord('a') + 1
y = int(xy[1])
cnt = 0

for m in move:
    dx = x + m[0]
    dy = y + m[1]
    if 0 < dx <= 8 and 0 < dy <= 8:
        cnt += 1
    dx -= m[0]
    dy -= m[1]

print(cnt)