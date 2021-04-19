def solution(s):
    stack = []
    for char in s:
        if char == '(':
            stack.append(char)
        else:
            if not stack:
                return False
            else:
                if stack[-1] == '(':
                    stack.pop()
                else:
                    return False
    return not stack


s = "(()("
print(solution(s))