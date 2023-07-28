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
import sys

s = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
sum = int(sys.stdin.readline())

arr.sort()
cnt = 0
i, j = 0, 0
if len(arr) <= 100000:
    for _ in range(len(arr)):
        num = arr[i] + arr[len(arr) - j - 1]
        if sum == num:
            cnt += 1
            i += 1
            j += 1
        elif sum > num:
            i += 1
        else:
            j += 1

        if i >= len(arr) - j - 1:
            break
print(cnt)