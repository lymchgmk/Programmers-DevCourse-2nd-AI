class MaxHeap:

    def __init__(self):
        self.data = [None]


    def insert(self, item):
        self.data.append(item)
        idx = len(self.data) - 1
        while idx != 1:
            how_may_parents = idx // 2
            if self.data[how_may_parents] < self.data[idx]:
                self.data[how_may_parents], self.data[idx] = self.data[idx], self.data[how_may_parents]
                idx = how_may_parents
            else:
                break


def solution(x):
    return 0