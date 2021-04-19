import itertools


def solution(m, weights):
    answer = 0
    is_picked = [[0, weight] for weight in weights]
    for case in itertools.product(*is_picked):
        if sum(case) == m:
            answer += 1
    return answer


m = 3000
weights = [500, 1500, 2500, 1000, 2000]
print(solution(m, weights))
