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

paper = [[0]*100 for _ in range(100)]

a = int(input())

matrix = []
for i in range(a):
    row = list(map(int, input().split()))
    matrix.append(row)

for i in matrix:
    for j in range(i[0], i[0]+10):
        for k in range(i[1], i[1]+10):
            paper[j][k] += 1

cnt = 0
for i in paper:
    for element in i:
        if element == 0:
            cnt += 1
print(10000-cnt)