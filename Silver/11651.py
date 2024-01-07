n = int(input())
l = []
for i in range(n):
    arr = list(map(int, input().split()))
    l.append(arr)
l.sort(key=lambda x: (x[1], x[0]))
for i in range(len(l)):
    for j in range(len(l[0])):
        print(l[i][j], end=' ')
    print()