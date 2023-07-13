class MaxHeap():
    def __init__(self, item=[]):
        self.item = item

    def lenght(self):
        return len(self.item)

    def _parent(self, cur_index):
        if cur_index == 0:
            return None
        return (cur_index - 1) // 2

    def _rchild(self, cur_index):
        return 2 * cur_index + 1

    def _lchild(self, cur_index):
        return 2 * cur_index + 2

    def shift_up(self, cur_index):
        '''从下至上'''
        while cur_index > 0 and self.item[self._parent(cur_index)] < self.item[cur_index]:
            self.item[self._parent(cur_index)], self.item[cur_index] = self.item[cur_index], self.item[
                self._parent(cur_index)]
            cur_index = self._parent(cur_index)
        return self.item

    def shift_down(self, cur_index):
        while self._lchild(cur_index) < self.lenght() - 1:
            if self.item[self._rchild(cur_index)] > self.item[self._lchild(cur_index)]:
                max_one = self._rchild(cur_index)
                if self.item[cur_index] < self.item[max_one]:
                    self.item[cur_index], self.item[max_one] = self.item[max_one], self.item[cur_index]
                    cur_index = max_one
                else:
                    break
            else:
                max_one = self._lchild(cur_index)
                if self.item[cur_index] < self.item[max_one]:
                    self.item[cur_index], self.item[max_one] = self.item[max_one], self.item[cur_index]
                    cur_index = max_one
                else:
                    break
        return self.item

    def insert(self, value):
        self.item.append(value)
        cur_index = self.lenght() - 1
        return self.shift_up(cur_index)

    def remove_top(self):
        self.item[0], self.item[-1] = self.item[-1], self.item[0]
        self.item.pop(-1)
        cur_index = 0
        return self.shift_down(cur_index)


if __name__ == '__main__':
    items = [12, 11, 10, 9, 6, 7, 8]
    m = MaxHeap(items)
    print(m.insert(13))
    print(m.remove_top())
