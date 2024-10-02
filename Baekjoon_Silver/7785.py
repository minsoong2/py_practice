import sys

num = int(sys.stdin.readline())
l = []
for i in range(num):
    l.append(sys.stdin.readline().split())
enter_l = []
for i in range(len(l)):
    if l[i][1] == 'enter':
        enter_l.append(l[i][0])
    elif l[i][1] == 'leave':
        enter_l.remove(l[i][0])
enter_l.sort(reverse=True)
for i in enter_l:
    print(i)