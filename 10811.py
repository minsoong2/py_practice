# import sys
# a, b, c = map(int, sys.stdin.readline().split())
# a = int(sys.stdin.readline())
# a, b = map(int, input().split())
# arr = list(map(int, input().split())) * list 공백기준 선언 *
# list -> int는 append x
# print(i, end=' ') end='' 줄바꿈 제거
# cnt = len(set(list)) * set -> 중복제거 *

# a = int(input())
# b = int(input())

a, b = map(int, input().split())

l = [0] * a
for i in range(a):
    l[i] = i + 1

arr = []
for i in range(b):
    c, d = map(int, input().split())
    arr = l[c-1:d][::-1]
    l[c-1:d] = arr

for i in range(a):
    print(l[i], end=' ')