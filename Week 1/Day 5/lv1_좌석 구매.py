from collections import Counter


def solution(seat):
    counter = Counter(map(tuple, seat))
    return len(counter)


seat = [[1,1],[2,1],[1,2],[3,4],[2,1],[2,1]]
print(solution(seat))
