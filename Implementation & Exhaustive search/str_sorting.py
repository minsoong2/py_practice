import sys

line = sys.stdin.readline().rstrip()
new_line = []
re = 0
for i in line:
    if (i == '1' or i == '2' or i == '3' or i == '4' or
        i == '5' or i == '6' or i == '7' or i == '8' or
        i == '9' or i == '0'):
        re += int(i)
    else:
        new_line.append(i)

new_line.sort()
for i in new_line:
    print(i, end='')
print(re)