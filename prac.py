# import sys
# a, b, c = map(int, sys.stdin.readline().split())
# a = int(sys.stdin.readline())
# a, b = map(int, input().split())
# arr = list(map(int, input().split())) * list 공백기준 선언 *
# list -> int는 append x
# print(i, end=' ') end='' 줄바꿈 제거
# cnt = len(set(list)) * set -> 중복제거 *

# l = [i for i in range(10)] * 파이썬 리스트 정의 *

# 정수 문자열 출력
# data = list(map(str, input().split()))
# num = int(data[0])
# string = data[1]

# a = int(input())
# b = int(input())

result_dict = {}
for i in range(10):
    result_dict[i] = 0

num = int(input())
p = 1
for j in range(len(str(num))):
    s = int(str(num//10) + "9")
    for i in range(10):
        result_dict[i] += (num//10+1) * p
    for i in range(10-(s-num), 10):
        result_dict[i] -= p
    for i in list(str(num)[:-1]):
        i = int(i)
        result_dict[i] -= (s-num) * p
    result_dict[0] -= p
    num //= 10
    p *= 10


for l in result_dict.values():
    print(l, end=' ')