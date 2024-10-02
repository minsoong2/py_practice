import sys

num = int(sys.stdin.readline())

for i in range(num):
    string = sys.stdin.readline()
    cnt_l = 0
    cnt_r = 0
    for j in range(len(string)):
        if cnt_l >= cnt_r:
            if string[j] == '(':
                cnt_l += 1
            elif string[j] == ')':
                cnt_r += 1
        else:
            break

    if cnt_r == cnt_l:
        print('YES')
    else:
        print('NO')