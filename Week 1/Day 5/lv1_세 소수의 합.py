from itertools import combinations


def solution(n):
    def is_prime(num):
        for i in range(2, int(num**0.5)+1):
            if not num % i:
                return False
        return True
    
    def find_prime_numbers(n):
        res = []
        for num in range(2, n):
            if is_prime(num):
                res.append(num)
        return res
    
    prime_numbers = find_prime_numbers(n)
    comb = combinations(prime_numbers, 3)
    answer = 0
    for c in comb:
        if sum(c) == n:
            answer += 1
    return answer


n = 9
print(solution(n))