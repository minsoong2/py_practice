# import sys
# a, b, c = map(int, sys.stdin.readline().split())
# a = int(sys.stdin.readline())
# a, b = map(int, input().split())
# arr = list(map(int, input().split())) * list 공백기준 선언 *
# list -> int는 append x
# print(i, end=' ') end='' 줄바꿈 제거
# cnt = len(set(list)) * set -> 중복제거 *
#

# a = int(input())
# b = int(input())

a = int(input())
sum = 0
for i in range(a):
    b = map(int, input())
    sum += b
print(sum)