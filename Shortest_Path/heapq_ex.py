import heapq

# python default - Min Heap
def min_heapsort(iterable):
    h = []
    result = []

    for value in iterable:
        heapq.heappush(h, value)
    print(h)

    for i in range(len(h)):
        result.append(heapq.heappop(h))

    return result

def max_heapsort(iterable):
    h = []
    result =[]

    for value in iterable:
        heapq.heappush(h, -value)
    print(h)

    for i in range(len(h)):
        result.append(-heapq.heappop(h))

    return result

print(min_heapsort([1, 3, 5, 7, 9, 2, 4, 6, 8, 0]))
print(max_heapsort([1, 3, 5, 7, 9, 2, 4, 6, 8, 0]))