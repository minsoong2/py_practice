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


def dictionary(string):

    result_dict = {}
    for char in string:
        result_dict[char] = result_dict.get(char, 0) + 1

    return result_dict


s = input()
lower_s = s.lower()
M = 0
alphabet = ''
for i in dictionary(lower_s):
    if M < dictionary(lower_s)[i]:
        M = dictionary(lower_s)[i]
        alphabet = i
    elif M == dictionary(lower_s)[i]:
        alphabet = '?'

print(alphabet.upper())