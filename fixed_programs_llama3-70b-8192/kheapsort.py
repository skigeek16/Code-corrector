def kheapsort(arr, k):
    import heapq

    heap = arr[:min(k, len(arr))]
    heapq.heapify(heap)

    for x in arr[k:]:
        yield heapq.heappush(heap, x)
        yield heapq.heappop(heap)

    while heap:
        yield heapq.heappop(heap)