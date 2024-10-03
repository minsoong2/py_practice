#
# def bi_search(arr, target, start, end):
#
#     while start <= end:
#         mid = (start + end) // 2
#
#         if arr[mid] == target:
#             return mid
#         elif arr[mid] > target:
#             end = mid - 1
#         else:
#             start = mid + 1
#
#     return None
#
# import sys
# m, target = map(int, sys.stdin.readline().split())
# num_list = list(map(int, sys.stdin.readline().split()))
#
# re = bi_search(num_list, target, 0, len(num_list) - 1)
#
# if re is None:
#     print('no data')
# else:
#     print(re + 1)