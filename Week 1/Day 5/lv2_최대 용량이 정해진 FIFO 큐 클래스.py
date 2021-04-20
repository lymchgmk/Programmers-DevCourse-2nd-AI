class MyStack(object):
    def __init__(self):
        self.lst = list()
    
    def push(self, x):
        self.lst.append(x)
    
    def pop(self):
        return self.lst.pop()
    
    def size(self):
        return len(self.lst)


class MyQueue(object):
    def __init__(self, max_size):
        self.stack1 = MyStack()
        self.stack2 = MyStack()
        self.max_size = max_size
    
    def qsize(self):
        # 구현하세요
        return self.stack1.size() + self.stack2.size()
    
    def push(self, item):
        # 구현하세요
        if self.qsize() == self.max_size:
            return False
        else:
            self.stack1.push(item)
            return True
    
    def pop(self):
        # 구현하세요
        try:
            if not self.stack2.size():
                while self.stack1.size():
                    self.stack2.push(self.stack1.pop())
            result = self.stack2.pop()
        except IndexError:
            return False
        return result


n, max_size = map(int, input().strip().split(' '))
my_queue = MyQueue(max_size)
for _ in range(n):
    op = list(map(str, input().strip().split()))
    if len(op) == 2:
        _, num = op
        print(my_queue.push(int(num)))
    else:
        if op == 'POP':
            print(my_queue.pop())
        elif op == 'SIZE':
            print(my_queue.qsize())
