import heapq
from collections import deque


def solution(healths, items):
    healths.sort()
    # idx, 포인트, 체력감소 를 1 부터 enumerate
    enum_items = [(idx, *item) for idx, item in enumerate(items, start=1)]
    IDX, POINT, HP_MINUS = 0, 1, 2
    # 감소체력 오름, 포인트 내림, idx 오름차순 정렬
    enum_items.sort(key=lambda x: (x[HP_MINUS], -x[POINT], x[IDX]))
    deq_enum_items = deque(enum_items)

    answer = []
    hq = []
    for health in healths:
        while deq_enum_items and health - deq_enum_items[0][HP_MINUS] >= 100:
            item = deq_enum_items.popleft()
            # -포인트, idx
            heapq.heappush(hq, (-item[POINT], item[IDX]))
        if hq:
            # idx 삽입
            answer.append(heapq.heappop(hq)[1])

    return sorted(answer)


healths = [200,120,150]
items = [[30,100],[500,30],[100,400]]
print(solution(healths, items))