# import sys
# a, b, c = map(int, sys.stdin.readline().split())
# a = int(sys.stdin.readline())
# a, b = map(int, input().split())
# arr = list(map(int, input().split())) * list 공백기준 선언 *
# list -> int는 append x
# print(i, end=' ') end='' 줄바꿈 제거
# cnt = len(set(list)) * set -> 중복제거 *

# 정수 문자열 출력
# data = list(map(str, input().split()))
# num = int(data[0])
# string = data[1]

# a = int(input())
# b = int(input())

a = int(input())

for i in range(1, a+1):
    print(' '*(a-i) + '*'*(2*i-1))

for j in range(a-1, 0, -1):
    print(' ' * (a - j) + '*' * (2 * j - 1))