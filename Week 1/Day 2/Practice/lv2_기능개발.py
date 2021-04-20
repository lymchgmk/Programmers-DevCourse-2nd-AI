def solution(progresses, speeds):
    que = []
    for p, s in zip(progresses, speeds):
        if not que or que[-1][0]<-((p-100)//s):
            que.append([-((p-100)//s), 1])
        else:
            que[-1][1] += 1
    return [q[1] for q in que]


progresses = [93,30,55]
speeds = [1, 30, 5]
print(solution(progresses, speeds))
