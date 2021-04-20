def solution(n, lost, reserve):
    gym_suit = [1]*(n+2)
    for i in reserve:
        gym_suit[i] += 1
    for i in lost:
        gym_suit[i] -= 1
    for i in range(1, n+1):
        if gym_suit[i-1] == 0 and gym_suit[i] == 2:
            gym_suit[i-1], gym_suit[i] = 1, 1
        elif gym_suit[i] == 2 and gym_suit[i+1] == 0:
            gym_suit[i], gym_suit[i+1] = 1, 1
    return len([gs for gs in gym_suit[1:-1] if gs])