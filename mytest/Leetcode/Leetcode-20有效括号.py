# 栈实现，先进后出，叠盘子
class Stack():
    def __init__(self):
        self.items = []

    def __add__(self, other):
        '''入栈'''
        self.items.append(other)

    def pop(self):
        '''出栈'''
        if len(self.items) > 0:
            self.items.pop(-1)

    def top(self):
        '''栈顶元素'''
        if len(self.items) > 0:
            return self.items[-1]

    def travel(self):
        for i in self.items:
            print(i, end=' ')


def match_(strs, ls, rs):
    kuohao = {
        '(': ')',
        '[': ']',
        '{': '}',
    }
    for i in list(strs):
        if i in kuohao.keys():
            ls.__add__(i)
        else:
            if kuohao.get(ls.top(), None) == i:
                ls.pop()
            else:
                rs.__add__(i)

    if len(rs.items) == 0 and len(ls.items) == 0:
        return True
    else:
        return False


if __name__ == '__main__':
    strs = '(()[[]({)}])'
    print(list(strs))
    ls = Stack()
    rs = Stack()
    result = match_(strs, ls, rs)
    print(result)
    # s = Stack()
    # s.__add__(0)
    # s.__add__(1)
    # s.__add__(2)
    # s.__add__(3)
    # s.pop()
    # s.top()
    # s.travel()
