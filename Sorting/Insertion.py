# 처리되지 않은 데이터를 적절한 위치에 삽입 O(n^2), 최선 O(N)

arr = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(1, len(arr)):
    for j in range(i, 0, -1):
        if arr[j] < arr[j - 1]:
            arr[j], arr[j - 1] = arr[j - 1], arr[j]
        else:
            break

print(arr)