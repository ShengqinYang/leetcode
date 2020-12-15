class Node(object):
    """单向链表的结点"""

    def __init__(self, elem):
        self.elem = elem
        self.next = None


class SingleLinkList(object):
    """单链表"""

    def __init__(self, node=None):
        """构造函数"""
        self.__head = node  # 头节点

    def getHead(self):
        return self.__head

    def travel(self):
        """遍历链表"""
        cur = self.__head
        while cur != None:
            print(cur.elem, end=" ")
            cur = cur.next
        print("")

    def add(self, item):
        """链表头部添加元素
        O(1)
        """
        node = Node(item)
        node.next = self.__head
        self.__head = node

    def listPartition1(self, num):  # 这种方法最快，但做不到稳定性，数组需要额外空间。
        # 普通问题
        # 时间复杂度是 O(N)，空间复杂度是 O(N)
        # 首先遍历一遍链表，得到链表的长度，将链表元素依次放到数组中，然后利用类似于快速排序中的partition 思想进行分割
        # partition完之后再串成链表
        if self.__head is None:  # 空链表
            return self.__head
        cur = self.__head
        i = 0
        while cur:  # 遍历一次链表，统计元素个数即链表长度
            cur = cur.next
            i += 1
        # 将链表中的每个元素依次放入到数组中
        nodeArr = []
        cur = self.__head
        for j in range(0, i):
            nodeArr.append(cur)
            cur = cur.next
        # print(i)

        # 进行类似快速排序的partition
        nodeArr = self.arrPartition(nodeArr, num)
        # 重新连接各个链表节点
        for q in range(1, i):
            nodeArr[q - 1].next = nodeArr[q]
        nodeArr[i - 1].next = None
        return nodeArr

    def arrPartition(self, nodeArr, num):
        left = -1
        right = len(nodeArr)
        index = 0
        while index < right:
            if nodeArr[index].elem < num:
                left += 1
                nodeArr[left], nodeArr[index] = nodeArr[index], nodeArr[left]  # 交换
                index += 1
            elif nodeArr[index].elem == num:
                index += 1
            else:
                right -= 1
                nodeArr[right], nodeArr[index] = nodeArr[index], nodeArr[right]  ##交换

        return nodeArr

    def listPartition2(self, num):  # 测试通过
        '''
     *  进阶问题： 保证各部分内部的顺序与原来链表中各个节点的顺序相同
     *  时间复杂度是 O(N)，空间复杂度是 O(1)
     *  考察 利用有限的几个变量来调整链表的代码实现能力。
    1.将链表分为三部分：small，equal，more
                      small：2->1->null
                      equal：5->5->null
                      more：9->7->8->null
    2.将small、equal、more三个链表重新串起来
    3.整个过程需要特别注意对null节点的判断和处理
        '''
        less = Node(None)
        endless = Node(None)
        equal = Node(None)
        endequal = Node(None)
        more = Node(None)
        endmore = Node(None)

        # every node distributed to three lists
        while self.__head:
            Next = self.__head.next
            self.__head.next = None
            if self.__head.elem < num:
                if less.elem is None:
                    less = self.__head
                    endless = self.__head
                else:
                    endless.next = self.__head
                    endless = endless.next
            elif self.__head.elem == num:
                if equal.elem is None:
                    equal = self.__head
                    endequal = self.__head
                else:
                    endequal.next = self.__head
                    endequal = self.__head
            elif self.__head.elem > num:
                if more.elem is None:
                    more = self.__head
                    endmore = self.__head
                else:
                    endmore.next = self.__head
                    endmore = self.__head
            self.__head = Next
        # small and equal reconnect
        if endless.elem and equal.elem:
            endless.next = equal
            endequal = endequal if endequal.elem else endless
        # all reconnect
        if endequal.elem:
            endequal.next = more
            endmore = endmore if endmore.elem else endequal
        res = equal if equal.elem else more
        res = less if less.elem else res  # 返回链表头节点
        return res

    def printLinkedList(self, node):
        print("Linked List:")
        while node.next:
            print(node.elem, end=" ")
            node = node.next
        print(node.elem)

    print("")


if __name__ == "__main__":
    s1 = SingleLinkList()
    s1.add(7)
    s1.add(9)
    s1.add(1)
    s1.add(8)
    s1.add(3)
    s1.add(5)
    s1.add(2)
    s1.add(5)
    s1.add(5)
    s1.add(4)
    s1.add(3)
    s1.travel()
    # res=s1.listPartition1(5)
    # s1.printLinkedList(res[0])
    # res = s1.listPartition2(6)  # bug:如果没有等于num的链表就断掉了
    # s1.printLinkedList(res)