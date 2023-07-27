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

l = [0] * 10
l_1 = [0] * 10

for i in range(10):
    l[i] = int(input())
    l_1[i] = l[i] % 42

cnt = len(set(l_1))
print(cnt)