'''
栈：先进后出，如：一摞叠在一起的盘子
应用场景：
    1.有效阔号的匹配，两个栈实现
    2.加减乘除运算优先级识别，两个栈实现
    3.浏览器的前进后退功能，两个栈实现
    4.函数调用栈，操作系统给每个线程分配了一块独立的内存空间，这块内存被组织成“栈”这种结构, 用来存储函数调用时的临时变量。每进入一个函数，就会将临时变量作为一个栈帧入栈，当被调用函数执行完成，返回之后，将这个函数对应的栈帧出栈
'''
from links.single_link import Node


class ArrayStack():
    '''数组实现的栈，顺序栈'''

    def __init__(self):
        self.stack = []

    def is_empty(self):
        '''判断是否为空'''
        return self.stack == []

    def push(self, item):
        '''入栈'''
        self.stack.append(item)

    def pop(self):
        '''出栈 '''
        if self.is_empty():
            print('stack is empty ~')
        else:
            self.stack.pop()

    def lenght(self):
        return len(self.stack)

    def top(self):
        '''返回栈顶元素'''
        if self.is_empty():
            print('stack is empty ~')
        else:
            print(self.stack[self.lenght() - 1])

    def travel(self):
        for i in range(self.lenght()):
            print(self.stack[i])


class LinkStack():
    '''链式栈'''

    def __init__(self, node=None):
        self.node = node

    def is_empty(self):
        '''栈是否为空'''
        return self.node == None

    def lenght(self):
        '''栈的长度'''
        cur = self.node
        count = 0
        while cur:
            count += 1
            cur = cur.next
        return count

    def push(self, item):
        '''入栈'''
        node = Node(item)
        if self.is_empty():
            self.node = node
        else:
            cur = self.node
            while cur.next:
                cur = cur.next
            cur.next = node

    def pop(self):
        '''出栈'''
        pre = None
        cur = self.node
        while cur.next:
            pre = cur
            cur = cur.next
        pre.next = None

    def top(self):
        '''返回栈顶元素'''
        cur = self.node
        while cur.next:
            cur = cur.next
        return cur.item

    def travel(self):
        '''遍历'''
        cur = self.node
        while cur:
            print('遍历', cur.item)
            cur = cur.next


# def match_brackets(bracket_str):
#     ''' 阔号有效匹配
#         有效：{[] ()[{}]}
#         无效：[}()]
#     '''
#     stckl = ArrayStack()
#     stckr = ArrayStack()
#     pei = {'{': '}',
#            '[': ']',
#            '(': ')'}
#     for v in list(bracket_str):
#         if v in pei.keys():
#             stckl.push(v)
#         else:
#             if pei.get(stckl.top()) == v:
#                 stckl.pop()
#             else:
#                 stckr.push(v)
#
#     if not stckl.is_empty() and not stckr.is_empty():
#         return True
#     else:
#         return False


def match_brackets(l, r, bracket_str):
    match = {"{": "}", "[": "]", "(": ")"}
    for i in list(bracket_str):
        if i in match.keys():
            l.push(i)
        else:
            if match.get(l.top()) == i:
                l.pop()
            else:
                r.push(i)

    if l.is_empty() and r.is_empty():
        return True
    else:
        return False


if __name__ == '__main__':
    # lts = ArrayStack()
    lts1 = ArrayStack()
    lts2 = ArrayStack()
    # print(lts.push("ysq"))
    # print(lts.push("zhd"))
    # print(lts.push("zps"))
    # print(lts.push("yyy"))
    # print(lts.is_empty())
    # print(lts.lenght())
    # # print(lts.pop())
    # print(lts.peek())

    # lks = LinkStack()
    # lks1 = LinkStack()
    # lks2 = LinkStack()
    # lks.push("ysq")
    # lks.push("zhd")
    # lks.push("zps")
    # lks.push("yyy")
    # # print(lks.is_empty())
    # print(lks.lenght())
    # # lks.travel()
    # lks.pop()
    # print('-------')
    # lks.travel()
    # print('-------')
    # print(lks.top())
    # print(check_str)
    result = match_brackets(lts1=lts1, lts2=lts2, check_str="{[] ()[{}]}")
    print(result)
