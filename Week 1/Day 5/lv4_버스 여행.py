from collections import deque


def solution(n, signs):
    # 갈 수 있는 곳 측정
    def _can_ride(start, sign):
        return deque([(start, dest) for dest, can_ride in enumerate(sign) if can_ride])

    answer = [[0] * n for _ in range(n)]
    for start, sign in enumerate(signs):
        deq = _can_ride(start, sign)
        while deq:
            curr, dest = deq.popleft()
            # 안가봤으면
            if not answer[curr][dest]:
                # 그 다음 갈 수 있는 곳을 뒤에 추가
                deq.extend(_can_ride(start, signs[dest]))
                # 가봤음 표시
                answer[curr][dest] = 1

    return answer


n = 3
signs = [[0,0,1],[0,0,1],[0,1,1]]
print(solution(n, signs))