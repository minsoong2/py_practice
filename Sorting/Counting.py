# 계수정렬
# 특정 조건일때 매우 빠름 
# 데이터 크기 범위가 제한 - 정수 형태로 표현할 수 있을 때 사용 가능
# 데이터 개수 N, 데이터(+) 중 최댓값 K -> 최악의 경우 O(N+K)
# 공간 복잡도 높음

# ex
# 7 5 9 0 3 1 6 2 9 1 4 8 0 5 2
# idx 0 1 2 3 4 5 6 7 8 9
# cnt 2 2 2 1 1 2 1 1 1 2
# cnt대로 출력!

arr = [7, 5, 9, 0, 3, 1, 6, 2, 9, 1, 4, 8, 0, 5, 2]
cnt_list = [0] * (max(arr) + 1)

for idx in arr:
    cnt_list[idx] += 1

for num in range(len(cnt_list)):
    for i in range(cnt_list[num]):
        print(num, end=" ")