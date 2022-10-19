'''
两数相加
题目：
    给出两个 非空 的链表用来表示两个非负的整数。其中，它们各自的位数是按照 逆序 的方式存储的，
    并且它们的每个节点只能存储 一位 数字。如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。
    您可以假设除了数字 0 之外，这两个数都不会以 0 开头。
示例：
    输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
    输出：7 -> 0 -> 8
    原因：342 + 465 = 807
考点：链表
'''


class Node():
    def __init__(self, item):
        self.item = item
        self.next = None


class Mycalss():

    def add_two_nums(self, node1, node2):
        if not node1:
            return node2
        if not node2:
            return node1
        val = node1.item + node2.item
        newnode = Node(val % 10)
        newnode.next = self.add_two_nums(node1.next, node2.next)
        if val >= 10:
            newnode.next = self.add_two_nums(Node(1), newnode.next)
        return newnode


if __name__ == '__main__':
    node1 = Node(2)
    node1.next = Node(4)
    node1.next.next = Node(3)

    # while True:
    #     if node1:
    #         print(node1.item, end=' ')
    #         node1 = node1.next
    #     else:
    #         break
    print('---')
    node2 = Node(5)
    node2.next = Node(6)
    node2.next.next = Node(4)
    # while True:
    #     if node2:
    #         print(node2.item, end=' ')
    #         node2 = node2.next
    #     else:
    #         break

    my = Mycalss()
    newnode = my.add_two_nums(node1, node2)
    print([newnode.item, newnode.next.item, newnode.next.next.item])
