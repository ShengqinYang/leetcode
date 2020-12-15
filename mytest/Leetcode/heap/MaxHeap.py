# 实现一个最大堆
class MaxHeap(object):
    """
    实现一个大顶堆
    """

    def __init__(self):
        self.array = []  # 用一个数组存放堆中元素

    def heapify(self, array):
        """
        对传入的数组进行堆化
        """
        for a in array:
            self.push(a)
        return self.array

    def get_size(self):
        """
        返回堆的大小
        """
        return len(self.array)

    def _parent(self, index):
        """
        返回某个节点的父节点
        """
        if index == 0:
            raise Exception('Index 0 has no parent')
        return int((index - 1) / 2)

    def _left_child(self, index):
        """
        返回左孩子节点的索引
        """
        return index * 2 + 1

    def _right_child(self, index):
        """
        返回右边孩子节点的索引
        """
        return index * 2 + 2

    def _shift_up(self, k):
        """
        节点上移动，将当前节点与其父亲节点比较大小，如果比父亲节点大，
        则交换其位置，重复只执行上述过程，直到当前节点比父亲节点小。
        """
        while k > 0 and self.array[self._parent(k)] < self.array[k]:
            # 交换节点与父节点的值
            self.array[self._parent(k)], self.array[k] = self.array[k], self.array[self._parent(k)]
            k = self._parent(k)

    def _shift_down(self, k):
        """
        节点下移动, 当前节点与它左右孩子中最大的节点交换位置
        """
        while self._left_child(k) < self.get_size():
            choose_index = self._left_child(k)  # 左孩子的索引
            # 先比较左右孩子的大小，选择较大的那个孩子再与父亲节点进行比较
            if choose_index + 1 < self.get_size() and self.array[choose_index + 1] > self.array[choose_index]:
                choose_index = self._right_child(k)
            if self.array[choose_index] <= self.array[k]:  # 如果最大的孩子比父亲节点小，退出循环
                break
            # 否则父亲节点和最大的子节点交换位置
            self.array[choose_index], self.array[k] = self.array[k], self.array[choose_index]
            k = choose_index  # 进行下次循环

    def push(self, value):
        """
        添加一个元素后，需要对堆重新进行堆化，具体过程就是对堆尾元素执行上移操作；
        """
        self.array.append(value)
        self._shift_up(self.get_size() - 1)  # 相当于对堆进行重新堆化

    def pop(self):
        """
        返回堆顶元素，将堆顶元素和堆最后一个元素交换，
        然后返回最后一个元素，最后对堆顶元素进行下沉操作（重新堆化）
        """
        ret = self.find_max()
        self.array[0], self.array[self.get_size() - 1] = self.array[self.get_size() - 1], self.array[0]
        self.array.pop(-1)  # 删除最后一个元素
        self._shift_down(0)
        return ret

    def find_max(self):
        """
        查看堆中的最大值
        """
        if self.array:
            return self.array[0]
        else:
            raise Exception('Empty heap has no value')


if __name__ == '__main__':
    # 测试我们实现的大顶堆
    test = [12, 11, 10, 9, 6, 7, 8, 13]
    max_heap = MaxHeap()
    print(max_heap.heapify(test))  # 对一个数组执行堆化
    print(max_heap.pop())  # 弹出堆顶元素
    print(max_heap.array)
    max_heap.push(14)  # 推入一个元素
    print(max_heap.array)
