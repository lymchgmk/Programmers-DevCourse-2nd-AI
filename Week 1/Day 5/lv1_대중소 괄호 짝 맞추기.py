def solution(s):
    chk_dict = {')': '(', ']': '[', '}': '{'}
    stack = []
    for chr in s:
        if chr in ('(', '[', '{'):
            stack.append(chr)
        else:
            if not stack:
                return False
            else:
                if chk_dict[chr] == stack[-1]:
                    stack.pop()
                else:
                    return False
    return not stack


s = "([())]"
print(solution(s))
