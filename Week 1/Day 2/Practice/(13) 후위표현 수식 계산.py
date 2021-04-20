class ArrayStack:

    def __init__(self):
        self.data = []

    def size(self):
        return len(self.data)

    def isEmpty(self):
        return self.size() == 0

    def push(self, item):
        self.data.append(item)

    def pop(self):
        return self.data.pop()

    def peek(self):
        return self.data[-1]


def splitTokens(exprStr):
    tokens = []
    val = 0
    valProcessing = False
    for c in exprStr:
        if c == ' ':
            continue
        if c in '0123456789':
            val = val * 10 + int(c)
            valProcessing = True
        else:
            if valProcessing:
                tokens.append(val)
                val = 0
            valProcessing = False
            tokens.append(c)
    if valProcessing:
        tokens.append(val)

    return tokens


def infixToPostfix(tokenList):
    prec = {
        '*': 3,
        '/': 3,
        '+': 2,
        '-': 2,
        '(': 1,
    }

    opStack = ArrayStack()
    postfixList = []
    for token in tokenList:
        if type(token) is int:
            postfixList.append(token)
        else:
            if token == '(':
                opStack.push(token)
            elif token == ')':
                while opStack.peek() != '(':
                    postfixList.append(opStack.pop())
                opStack.pop()
            else:
                if opStack.isEmpty():
                    opStack.push(token)
                else:
                    while opStack.size():
                        if prec[opStack.peek()] >= prec[token]:
                            postfixList.append(opStack.pop())
                        else:
                            break
                    opStack.push(token)
                    
    while not opStack.isEmpty():
        postfixList.append(opStack.pop())
        
    return postfixList


def postfixEval(tokenList):
    valStack = ArrayStack()
    for token in tokenList:
        if type(token) is int:
            valStack.push(token)
        else:
            n1 = valStack.pop()
            n2 = valStack.pop()
            if token == '+':
                valStack.push(n2 + n1)
            elif token == '-':
                valStack.push(n2 - n1)
            elif token == '*':
                valStack.push(n2 * n1)
            elif token == '/':
                valStack.push(n2 // n1)
    
    return valStack.pop()
            

def solution(expr):
    tokens = splitTokens(expr)
    postfix = infixToPostfix(tokens)
    val = postfixEval(postfix)
    return val


S = '(1+2)*(3+4)'
print(solution(S))