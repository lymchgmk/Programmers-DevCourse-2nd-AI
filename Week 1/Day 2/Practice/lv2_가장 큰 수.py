def solution(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key=lambda x: (x[0 % len(x)], x[1 % len(x)], x[2 % len(x)], x[3 % len(x)]), reverse=True)
    answer = ''.join(numbers)
    return answer if int(answer) else '0'


numbers = [6, 10, 2]
print(solution(numbers))