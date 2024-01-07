a, b = map(int, input().split())
l = []
for i in range(1, a+1):
    if a % i == 0:
        l.append(i)
l.sort()
try:
    print(l[b - 1])
except:
    print(0)