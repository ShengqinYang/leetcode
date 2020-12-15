class WangHeap:
    '''
    https://www.jianshu.com/p/57a814462e39
    1.堆的定义：
        必须是完全二叉树【定义：除了最后一层，其他层必须是满叶子，且最后一层叶子必须靠左侧排列】
        满足所有父节点都大于等于（或者小于等于，即：小顶堆）他的左右子节点，即：大顶堆
    2.大顶堆
    3.小顶堆
    4.列表实现大顶堆如：[31,23,15,16,8,9,7,11]
                        31
                    23      15
                  16   8  9   7
                11
        公式：父节点 = i/2 , 左子节点 = i*2 ，右子节点 = i*2+1  【其中i为列表中的第几位元素，(下标从1开始)即下标】
        公式：父节点 = i-1/2 , 左子节点 = i*2+1 ，右子节点 = i*2+2  【其中i为列表中的第几位元素，(下标从0开始)即下标】
             父节点 = 右节点-左节点
    需掌握：
    1.堆的插入，自下而上的堆化过程  【√】
    2.堆顶元素删除，自上而下的堆化过程 【√】
    3.堆排序 【🔘】
    '''

    def __init__(self, capacity, items=[]):
        self.capacity = capacity  # 堆的最大容量
        self.items = items

    @property
    def lenght(self):
        '''堆现在大小'''
        return len(self.items)

    def _parent(self, index):
        '''父节点,索引'''
        return (index - 1) // 2

    def _left(self, index):
        '''左子点,索引'''
        return index * 2 + 1

    def _right(self, index):
        '''右子节点,索引'''
        return index * 2 + 2

    def _shift_up(self, cur_index):
        '''从下至上的堆化过程'''
        while cur_index > 0 and self.items[self._parent(cur_index)] < self.items[cur_index]:
            # 父子比较大小
            self.items[self._parent(cur_index)], self.items[cur_index] = self.items[cur_index], self.items[
                self._parent(cur_index)]
            cur_index = self._parent(cur_index)
        return self.items

    def _shift_down(self, cur_index):
        '''从上至下的堆化过程'''
        while self._left(cur_index) < self.lenght - 1:  # 左子节点小于 总堆长度
            if self.items[self._left(cur_index)] > self.items[self._right(cur_index)]:  # 找出子节点里大的一个
                max = self._left(cur_index)
                if self.items[cur_index] < self.items[max]:  # 父子比较
                    self.items[cur_index], self.items[max] = self.items[max], self.items[cur_index]
                    cur_index = self._left(cur_index)
                else:
                    break
            else:
                max = self._right(cur_index)
                if self.items[cur_index] < self.items[max]:  # 父子比较
                    self.items[cur_index], self.items[max] = self.items[max], self.items[cur_index]
                    cur_index = self._right(cur_index)
                else:
                    break
        return self.items

    def insert(self, item):
        '''
        堆里添加一个值，堆化过程，采取从下至上的堆化过程
        :param item:
        :return:
        '''
        if self.lenght <= 0:
            self.items.append(item)
            return
        elif self.lenght > self.capacity:
            return
        else:
            self.items.append(item)
        cur_index = self.lenght - 1  # 当前索引
        return self._shift_up(cur_index)

    def remove_top(self):
        '''删除堆顶元素，堆化过程，采取从上至下的堆化过程
        '''
        if self.lenght <= 0:
            return
        elif self.lenght == 1:
            self.items = []
            return self.items
        else:
            self.items[0], self.items[-1] = self.items[-1], self.items[0]  # 首尾节点交换
            self.items.pop()  # 删除尾节点，即删除堆顶元素，删完后需要重新堆化
            cur_index = 0
            return self._shift_down(cur_index)


if __name__ == '__main__':
    max_capacity = 100
    myheap = WangHeap(max_capacity, items=[])
    myheap.insert(1)
    myheap.insert(2)
    myheap.insert(13)
    myheap.insert(4)
    rs = myheap.insert(16)
    print(rs)
    nrs = myheap.remove_top()
    print(nrs)
