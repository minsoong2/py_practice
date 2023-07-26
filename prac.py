# import sys
# a, b, c = map(int, sys.stdin.readline().split())
# a = int(sys.stdin.readline())
# a, b = map(int, input().split())
# arr = list(map(int, input().split()))
# print(i, end=' ') end='' 줄바꿈 제거

a, b = map(int, input().split())
# b = int(input())

arr = list(map(int, input().split()))

for i in arr:
    if i < b:
        print(i, end=' ')
