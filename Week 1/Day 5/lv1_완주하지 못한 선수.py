import collections


def solution(participant, completion):
    counter_participant = collections.Counter(participant)
    counter_participant.subtract(completion)
    return counter_participant.most_common(1)[0][0]