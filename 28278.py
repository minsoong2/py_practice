import sys

num = int(sys.stdin.readline())
l = []
for i in range(num):
    string = sys.stdin.readline().split()
    if string[0] == '1':
        l.append(int(string[1]))
    elif string[0] == '2':
        if len(l) != 0:
            print(l.pop())
        else:
            print(-1)
    elif string[0] == '3':
        print(len(l))
    elif string[0] == '4':
        if len(l) == 0:
            print(1)
        else:
            print(0)
    elif string[0] == '5':
        if len(l) == 0:
            print(-1)
        else:
            print(l[-1])