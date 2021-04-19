from bisect import bisect_left, bisect


def solution(L, x):
    idx = bisect(L, x)
    return idx-1 if L[idx-1] == x else -1


L = [2, 3, 5, 6, 9, 11, 15]
x = 6
print(solution(L, x))