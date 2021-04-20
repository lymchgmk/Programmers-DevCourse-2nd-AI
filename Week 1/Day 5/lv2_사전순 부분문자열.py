# def solution(s):
#     def powerset(s):
#         masks = [1 << i for i in range(len(s))]
#         for i in range(1 << len(s)):
#             yield [ss for ss, mask in zip(s, masks) if mask & i]
#
#     cand = [''.join(sub) for sub in powerset(s)]
#     cand.sort(reverse=True)
#     return cand[0]


def solution(s):
    stack = []
    for c in s:
        while stack and stack[-1] < c:
            stack.pop()
        stack.append(c)
    return ''.join(stack)

s = "yxyc"
print(solution(s))