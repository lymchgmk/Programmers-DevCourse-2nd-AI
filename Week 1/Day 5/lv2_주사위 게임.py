def solution(monster, S1, S2, S3):
    cnt = 0
    for dice1 in range(1, S1+1):
        for dice2 in range(1, S2+1):
            for dice3 in range(1, S3+1):
                dice = dice1 + dice2 + dice3 + 1
                if dice not in monster:
                    cnt += 1

    total_cases = S1 * S2 * S3
    return int((cnt / total_cases)*1000)
    


monster = [4,9,5,8]
S1 = 2
S2 = 3
S3 = 3
print(solution(monster, S1, S2, S3))
