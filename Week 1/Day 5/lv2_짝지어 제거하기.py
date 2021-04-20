# import re
#
#
# def solution(s):
#     tmp = re.sub(r'(\w)\1', '', s)
#     while tmp != s:
#         s = tmp
#         tmp = re.sub(r'(\w)\1', '', s)
#     return 1 if not s else 0


def solution(s):
    stack = []
    for c in s:
        if not stack:
            stack.append(c)
        else:
            if stack[-1] == c:
                stack.pop()
            else:
                stack.append(c)
    
    return 1 if not stack else 0
        


s = 'baabaa'
print(solution(s))
