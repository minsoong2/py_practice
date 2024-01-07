n = int(input())
l = []
for i in range(n):
    data = list(map(str, input().split()))
    num = int(data[0])
    string = data[1]
    l.append((num, string))
l.sort(key=lambda x: x[0])
for i in range(len(l)):
    for j in range(len(l[0])):
        print(l[i][j], end=' ')
    print()