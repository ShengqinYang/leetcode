"""
定义一个单链表：
单链表定义：每个节点都有一个值和一个指针指向下一个节点的位置
单链表具备的方法【参照list】：
    1.一个节点类，两个变量，value 和 next
    2.链表类：
        1）.初始化单链表，
        2）.判断链表是否为空
        3）.头部插入
        4）.尾部添加
        5）.指定位置插入
        6）.遍历链表
        7）.获得链表长度
        8）.判断一个节点是否存在
        9）.删除一个节点，指定值删除remove

        10）.单链表反转reverse  还没写
        11）.链表中环的检测
        12）.两个有序的链表合并
        13）.删除链表倒数第 n 个结点
        14）.求链表的中间结点
        15）.链表两两反转，例如：1-2-3-4 --> 2-1-4-3
应用场景：如何用链表来实现 最近最少使用策略LRU 缓存淘汰策略呢？
"""


class Node():
    def __init__(self, item):
        self.item = item
        self.next = None


class SingleLink():
    def __init__(self, node=None):
        ''' 1）.初始化单链表，'''
        self.head = node

    @property
    def is_empty(self):
        '''2）.判断链表是否为空'''
        if self.head == None:
            return True
        else:
            return False

    def add(self, item):
        '''3）.头部插入'''
        node = Node(item)
        node.next = self.head
        self.head = node

    def append(self, item):
        '''4）.尾部添加 '''
        node = Node(item)
        if self.is_empty:
            self.add(item)
        else:
            cur = self.head
            while cur.next != None:
                cur = cur.next
            cur.next = node

    def insert(self, item, pos):
        ''' 5）.指定位置插入
        :param item: 值，start 0
        :param pos: 位置
        :return:
        '''
        if pos <= 0:
            '''pos小于当前链表长度'''
            self.add(item)
        elif pos > self.lenght() - 1:
            '''pos超出当前链表长度'''
            self.append(item)
        else:
            node = Node(item)
            cur_pos = 0
            cur = self.head
            while cur_pos < pos - 1:
                cur_pos += 1
                cur = cur.next
            node.next = cur.next
            cur.next = node

    @property
    def travel(self):
        '''6）.遍历链表'''
        cur = self.head
        while cur != None:
            print(cur.item, end=' ')
            cur = cur.next

    @property
    def lenght(self):
        '''7）.获得链表长度'''
        if self.is_empty:
            return 0
        else:
            count = 1
            cur = self.head
            while cur.next != None:
                count += 1
                cur = cur.next
            return count

    def find(self, item):
        '''8）.判断一个节点是否存在'''
        cur = self.head
        while cur != None:
            if cur.item == item:
                return True
            cur = cur.next
        return False

    def remove(self, item):
        '''9）.删除一个节点，指定值删除remove'''
        cur = self.head
        pre = None
        while cur != None:
            if cur.item == item:
                if cur == self.head:  # 判断当前节点是不是头节点
                    self.head = cur.next
                else:
                    pre.next = cur.next
                break
            else:
                pre = cur
                cur = cur.next

    def remove_n_from_end(self, n):
        '''
        13）.删除链表倒数第 n 个结点
        '''
        lenght = self.lenght
        if n > lenght:
            raise IndexError("index out of range.")
        else:
            pre = self.head
            cur = self.head
            re_pos = lenght - n
            count = 0
            while cur != None:
                if count == re_pos:
                    if cur == self.head:
                        self.head = cur.next
                    else:
                        pre.next = cur.next
                    break
                else:
                    pre = cur
                    cur = cur.next
                    count += 1

    @property
    def middle_node(self):
        """
        14）.求链表的中间结点
        使用快慢节点：慢的走1步，快的走2步，快的节点和快的节点的下个节点为真则继续，否则 return slow.item
        """
        fast = self.head
        slow = self.head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        return slow.item


class Solution():
    def reverse(self, link):
        '''10）.单链表反转reverse  利用哨兵，时间复杂度O(n)'''
        cur = link.head
        pre = None
        while cur:
            temp = cur.next
            cur.next = pre
            pre = cur
            cur = temp
        return pre

    def swap_pairs(self, link):
        '''
         15）.链表两两反转，例如：1-2-3-4 --> 2-1-4-3
        '''
        pre, pre.next = link, link.head
        while pre.next and pre.next.next:
            a = pre.next
            b = a.next
            pre.next, b.next, a.next = b, a, b.next
            pre = a
        return link.next

    def merge(self, l1, l2):
        '''
        12）.两个有序的链表合并
        题：将两个升序链表合并为一个新的升序链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。
        例如：
            输入：1->2->4, 1->3->4
            输出：1->1->2->3->4->4
        '''
        l1 = l1.head
        l2 = l2.head
        node = Node(0)
        l3 = node
        while l1 and l2:
            if l1.item >= l2.item:
                l3.next = l2
                l2 = l2.next
            else:
                l3.next = l1
                l1 = l1.next
            l3 = l3.next
        if l1:
            l3.next = l1
        if l2:
            l3.next = l2
        return node

    def check_circle(self, link):
        '''11）.链表中环的检测,快慢指针法，如果有环，那么快指针绕一圈会和慢指针重合,时间复杂度O(n)'''
        fast = link.head
        slow = link.head
        while slow and fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow is fast:  # 易错点：是item和next都相等，错误写法：fast.item == slow.item
                return True
        return False


def travel_link(link):
    cur = link.head
    while cur:
        print(cur.item, end=' ')
        cur = cur.next


if __name__ == '__main__':
    # mylink = SingleLink()
    # mylink.add(2)
    # mylink.add(1)
    # mylink.append(3)
    # mylink.append(4)
    # mylink.append(5)
    # mylink.append(6)
    # mylink.append(7)
    # mylink.append(8)
    # l = mylink.lenght
    # print('长度', l)
    # mylink.travel  # 遍历
    # mylink.insert(56, -9)
    # print(' ')
    # mylink.travel
    # print(' ')
    # print('查找', mylink.find(3))
    # mylink.remove(2)
    # mylink.travel
    # middle_node = mylink.middle_node
    # print('middle_node节点：', middle_node)
    # mylink.remove_n_from_end(2)
    # mylink.travel
    # print(mylink.reverse)
    # mylink.travel
    l1 = SingleLink()
    l1.append(1)
    l1.append(2)
    l1.append(3)
    l1.append(4)
    l2 = SingleLink()
    l2.append(8)
    l2.append(9)
    l2.append(10)
    # print(l1.head)

    s = Solution()
    # 合并
    # m = s.merge(l1, l2)
    # print(m)
    # travel_link(m)
    # 反转
    # result = s.reverse(l1)
    # travel_link(result)
    # 检测环
    # print(s.check_circle(l1))
    # 两两交换
    # travel_link(l1)
    r = s.swap_pairs(l1)
    print(r.item, r.next.item, r.next.next.item, r.next.next.next.item)
    travel_link(r)
