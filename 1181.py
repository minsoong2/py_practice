n = int(input())
l = []
for i in range(n):
    l.append(input())
l = list(set(l))
l.sort(key=lambda x: (len(x), x))
for i in range(len(l)):
    print(l[i])