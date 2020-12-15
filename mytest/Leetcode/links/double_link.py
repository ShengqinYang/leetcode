class DNode():
    def __init__(self, item):
        self.item = item
        self.prev = None
        self.next = None


class DoubleLink():
    def __init__(self, head=None):
        self.head = head

    def is_empty(self):
        if self.head == None:
            return True
        else:
            return False

    def lenght(self):
        cur = self.head
        count = 1
        while cur.next:
            count += 1
            cur = cur.next
        return count

    def head_add(self, item):
        '''3）.头部插入'''
        node = DNode(item)
        if self.is_empty():
            self.head = node
            self.head.next = None
            self.head.prev = None
        else:
            node.next = self.head
            self.head.prev = node
            self.head = node
            self.head.prev = None

    def append(self, item):
        if self.is_empty():
            self.head_add(item)
        else:
            node = DNode(item)
            cur = self.head
            while cur.next:
                cur = cur.next
            node.prev = cur
            cur.next = node

    def get(self, item):
        cur = self.head
        while cur:
            if cur.item == item:
                return True
            cur = cur.next
        return False

    def delete(self, index):
        '''
        删除第几个
        :param index:
        :return:
        '''
        if self.lenght() < index:
            raise Exception('index out of range')
        else:
            count = 0
            cur = self.head
            while cur.next:
                if count == index:
                    if index == 0:
                        self.head = cur.next
                    else:
                        cur.prev.next = cur.next
                        cur.next.prev = cur.prev
                    break
                else:
                    cur = cur.next
                    count += 1

    def travel(self):
        cur = self.head
        while cur:
            print(cur.item, end=' ')
            cur = cur.next


if __name__ == '__main__':
    dlink = DoubleLink()
    dlink.head_add(1)
    dlink.head_add(2)
    dlink.head_add(3)
    dlink.append(5)
    dlink.append(6)
    dlink.append(7)
    dlink.append(8)
    dlink.travel()
    r = dlink.get(5)
    print(r)
    dlink.delete(5)
    dlink.travel()
