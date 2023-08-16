import sys

string = sys.stdin.readline().strip('\n')

l = []
for i in range(len(string)):
    for j in range(len(string)):
        l.append(string[i:i+j+1])
        if i+j+1 == len(string):
            break
print(len(set(l)))