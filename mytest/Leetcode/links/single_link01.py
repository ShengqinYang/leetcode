class SNode():
    '''
    单链表节点
    '''

    def __init__(self, item):
        self.item = item
        self.next = None


class SingleLink():
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
        node = SNode(item)
        node.next = self.head
        self.head = node

    def append(self, item):
        if self.is_empty():
            self.head_add(item)
        else:
            node = SNode(item)
            cur = self.head
            while cur.next != None:
                cur = cur.next
            cur.next = node

    def insert(self, index, item):
        node = SNode(item)
        cur = self.head
        count = 0
        while cur.next and index < count - 1:
            cur = cur.next
            count += 1
        node.next = cur.next
        cur.next = node

    def delete(self, index):
        '''

        :param index:
        :return:
        '''
        if self.lenght() < index + 1:
            return 'index out of range'
        else:
            cur = self.head
            prev = self.head
            count = 0
            while cur:
                if count == index:
                    if cur == self.head:
                        self.head = cur.next
                    else:
                        prev.next = cur.next
                    break
                else:
                    prev = cur
                    cur = cur.next
                    count += 1

    def find(self, item):
        pass

    def travel(self):
        cur = self.head
        while cur:
            print(cur.item, end=' ')
            cur = cur.next


def reverse(link):
    cur = link.head
    pre = None
    while cur:
        temp = cur.next
        cur.next = pre
        pre = cur
        cur = temp
    return pre


def check_circle(link):
    fast = link.head
    slow = link.head
    while fast and fast.next and slow:
        fast = fast.next.next
        slow = slow.next
        if fast == slow:  # 易错点：是item和next都相等，错误写法：fast.item == slow.item
            return True
    return False


def merge(link1, link2):
    '''有序链表合并'''
    l1 = link1.head
    l2 = link2.head
    n = SNode(0)
    l3 = n
    while l1 and l2:
        if l1.item >= l2.item:
            l3.next = l2.item
            l2 = l2.next
        else:
            l3.next = l1.item
            l1 = l1.next
        l3 = l3.next
    if l1:
        l3.next = l1
    if l2:
        l3.next = l2
    return n


def middle_node(link):
    '''
     14）.求链表的中间结点
        使用快慢节点：慢的走1步，快的走2步，快的节点和快的节点的下个节点为真则继续，否则 return slow.item
    '''
    fast = link.head
    slow = link.head
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
    return slow.item


if __name__ == '__main__':
    slink = SingleLink()
    slink.head_add(2)
    slink.append(2)
    slink.append(2)
    slink.append(2)
    slink.append(3)
    slink.append(4)
    slink.append(5)
    # slink.delete(2)
    slink.travel()
    result = check_circle(slink)
    print(result)
