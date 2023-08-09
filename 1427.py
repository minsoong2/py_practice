s = input()
l = []
for i in range(len(s)):
    l.append(int(s[i]))
l.sort(reverse=True)
for i in range(len(l)):
    print(l[i], end='')