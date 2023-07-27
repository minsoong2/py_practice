# import sys
# a, b, c = map(int, sys.stdin.readline().split())
# a = int(sys.stdin.readline())
# a, b = map(int, input().split())
# arr = list(map(int, input().split())) list 공백기준 선언
# print(i, end=' ') end='' 줄바꿈 제거

# a = int(input())
# b = int(input())


a, b = map(int, input().split())

l = [0] * a

for i in range(b):
    c, d, e = map(int, input().split())
    for j in range(c-1, d):
        l[j] = e

for i in range(len(l)):
    print(l[i], end=' ')