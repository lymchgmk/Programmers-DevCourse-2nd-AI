from collections import Counter


def solution(participnt, completion):
    count_part = Counter(participnt)
    count_comp = Counter(completion)
    for key in count_part:
        if count_part[key] != count_comp[key]:
            return key
