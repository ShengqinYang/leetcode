'''
队列：先进先出
数组实现的队列叫顺序队列
链表实现的队列叫链式队列
头尾指针，循环队列，阻塞队列，并发队列
'''
from itertools import chain

from links.single_link import Node


class ArrayQueue():
    def __init__(self):
        self.queue = []

    def is_empty(self):
        return self.queue == []

    def lenght(self):
        return len(self.queue)

    def enqueue(self, item):
        '''入队列'''
        self.queue.append(item)

    def dequeue(self):
        '''出队列'''
        item = self.queue.pop(0)
        return item


class LinkQueue():
    def __init__(self):
        self.node = None

    def is_empty(self):
        return self.node == None

    def lenght(self):
        cur = self.node
        count = 0
        while cur:
            count += 1
            cur = cur.next
        return count

    def enqueue(self, item):
        '''入队列'''
        node = Node(item)
        if self.is_empty():
            node.next = self.node
            self.node = node
        else:
            cur = self.node
            while cur.next:
                cur = cur.next
            cur.next = node

    def dequeue(self):
        '''出队列'''
        if self.is_empty():
            print('队列为空')
        else:
            cur = self.node
            self.node = cur.next


class circle_queue():
    '''
    循环队列，关键在于判断对空和队满的判断条件,队尾下标值=(tail + 1)%n
    对空：head==tail
    对满：(tail + 1)%n == head 注意：这样实际上会有一个空位子

    '''

    def __init__(self, capacity):
        self._items = []  # 数组
        self._head = 0  # 头指针
        self._tail = 0  # 尾指针
        self._capacity = capacity + 1  # 数组大小，因为会空一格位置，为了充分利用数组位置，所以+1

    def enqueue(self, item):
        '''入队列，注意变更尾指针的位置'''
        if (self._tail + 1) % self._capacity == self._head:  # 判断队满
            return False

        self._items.append(item)
        self._tail = (self._tail + 1) % self._capacity
        return True

    def dequeue(self):
        '''出队列，注意变更头指针的位置'''
        if self._tail != self._head:
            item = self._items[self._head]
            # self._items.pop(self._head)
            self._head = (self._head + 1) % self._capacity
            return item

    def __repr__(self):
        if self._tail >= self._head:
            return " ".join(i for i in self._items[self._head:self._tail])
        else:
            return " ".join(i for i in chain(self._items[self._head:], self._items[:self._tail]))


if __name__ == '__main__':
    # q = ArrayQueue()
    # q = LinkQueue()
    q = circle_queue(5)
    q.enqueue("a")
    q.enqueue("b")
    q.enqueue("c")
    q.enqueue("d")
    q.dequeue()
    # q.enqueue("5")
    # q.enqueue("6")
    # q.dequeue()
    # q.dequeue()
    # q.dequeue()
    # q.enqueue("7")
    # q.enqueue("8")
    print(len(q._items))
    for i in q._items:
        print('sd', i)
    # q.dequeue()
    # print(q.lenght())
    print(q)
    # print(q.queue)
    # print(q.is_empty())
