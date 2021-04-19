def solution(v):
    answer = {'x': [], 'y': []}
    for x, y in v:
        if x not in answer['x']:
            answer['x'].append(x)
        else:
            answer['x'].remove(x)
        if y not in answer['y']:
            answer['y'].append(y)
        else:
            answer['y'].remove(y)
    
    return [answer['x'][0], answer['y'][0]]
    
    
v = [[1, 1], [2, 2], [1, 2]]
print(solution(v))
