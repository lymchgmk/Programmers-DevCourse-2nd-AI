import heapq


def solution(n, works):
    if sum(works) <= n:
        return 0
    
    works = [-work for work in works]
    heapq.heapify(works)
    for _ in range(n):
        need_work = heapq.heappop(works)
        heapq.heappush(works, need_work+1)
    
    return sum([work**2 for work in works])
