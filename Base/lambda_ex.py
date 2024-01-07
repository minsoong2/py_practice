# 기존의 함수 정의
def add(x, y):
    return x + y


result1 = add(3, 5)
print(result1)  # 출력: 8

add_lambda = lambda x, y: x + y

result2 = add_lambda(3, 5)
print(result2)  # 출력: 8