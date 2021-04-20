from heapq import heapify, heappush, heappop


def solution(N, works):
    if N > sum(works):
        return 0
    
    minus_works = [-work for work in works]
    heapify(minus_works)
    for _ in range(N):
        need_work = heappop(minus_works)
        heappush(minus_works, need_work+1)
    return sum([minus_work**2 for minus_work in minus_works])


N = 4
works = [4, 3, 3]
print(solution(N, works))
