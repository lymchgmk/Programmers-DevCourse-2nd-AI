from collections import deque


def solution(max_weight, specs, names):
    answer = 0
    specs_dict = {name: int(weight) for name, weight in specs}
    names_deque = deque(names)
    truck = 0
    while names_deque:
        name = names_deque.popleft()
        truck += specs_dict[name]
        if truck > max_weight:
            answer += 1
            truck = 0
            names_deque.appendleft(name)
            
    if truck:
        answer += 1
        
    return answer


max_weight = 200
specs = [["toy","70"], ["snack", "200"]]
names = ["toy", "snack", "toy"]
print(solution(max_weight, specs, names))
