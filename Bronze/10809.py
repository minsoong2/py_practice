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

s = input()

l = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
     'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
arr = [-1] * 26
for i in range(len(s)):
    if s[i] in l:
        arr[l.index(s[i])] = s.index(s[i])

for i in range(len(l)):
    print(arr[i], end=' ')