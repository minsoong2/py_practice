import sys

# input_data = input()
# row = int(ord(input_data[0])) - int(ord('a')) + 1
# col = int(input_data[1])
# ord: 문자 -> ASCII
# chr: ASCII -> 문자

x, y = 0, 0

while True:
    xy = sys.stdin.readline()

    if xy[0] == 'a':
        x = 1
    elif xy[0] == 'b':
        x = 2
    elif xy[0] == 'c':
        x = 3
    elif xy[0] == 'd':
        x = 4
    elif xy[0] == 'e':
        x = 5
    elif xy[0] == 'f':
        x = 6
    elif xy[0] == 'g':
        x = 7
    elif xy[0] == 'h':
        x = 8
    else:
        print('error')
        continue
    y = int(xy[1])
    break

move_cnt = 0
for cnt in range(8):
    if cnt == 0:
        x += 2
        y += 1
        if 1 <= x <= 8 and 1 <= y <= 8:
            move_cnt += 1
        x -= 2
        y -= 1
    elif cnt == 1:
        x += 2
        y -= 1
        if 1 <= x <= 8 and 1 <= y <= 8:
            move_cnt += 1
        x -= 2
        y += 1
    elif cnt == 2:
        x -= 2
        y += 1
        if 1 <= x <= 8 and 1 <= y <= 8:
            move_cnt += 1
        x += 2
        y -= 1
    elif cnt == 3:
        x -= 2
        y -= 1
        if 1 <= x <= 8 and 1 <= y <= 8:
            move_cnt += 1
        x += 2
        y += 1
    elif cnt == 4:
        y += 2
        x += 1
        if 1 <= x <= 8 and 1 <= y <= 8:
            move_cnt += 1
        y -= 2
        x -= 1
    elif cnt == 5:
        y += 2
        x -= 1
        if 1 <= x <= 8 and 1 <= y <= 8:
            move_cnt += 1
        y -= 2
        x += 1
    elif cnt == 6:
        y -= 2
        x += 1
        if 1 <= x <= 8 and 1 <= y <= 8:
            move_cnt += 1
        y += 2
        x -= 1
    elif cnt == 7:
        y -= 2
        x -= 1
        if 1 <= x <= 8 and 1 <= y <= 8:
            move_cnt += 1
        y += 2
        x += 1

print(move_cnt)