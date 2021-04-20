def solution(d, budget):
    d.sort()
    answer = 0
    total_price = 0
    for price in d:
        total_price += price
        if total_price <= budget:
            answer += 1
    return answer