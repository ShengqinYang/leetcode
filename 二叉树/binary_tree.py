class Node():
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Tree:
    def __init__(self):
        self.root = None

    def add(self, val):
        node = Node(val)
        if self.root is None:
            self.root = node  # val 只是一个值不是树行结构，节点应该是一个树行结构，所以等于Node(val)
            return

        queue_list = [self.root]
        while queue_list:
            curnode = queue_list.pop(0)
            if curnode.left is None:
                curnode.left = node
                return
            else:
                queue_list.append(curnode.left)
            if curnode.right is None:
                curnode.right = node
                return
            else:
                queue_list.append(curnode.right)

    def brea_travel(self):
        queue_list = [self.root]
        if self.root is None:
            print('empyt')
            return
        while queue_list:
            curnode = queue_list.pop(0)
            print(curnode.val)
            if curnode.left is not None:
                queue_list.append(curnode.left)
            if curnode.right is not None:
                queue_list.append(curnode.right)
        return ''


tree = Tree()
tree.add(1)
tree.add(2)
tree.add(3)
tree.add(4)
tree.add(5)
# print(tree.brea_travel())


class Solution:
    def run(self, root):
        if root is None:
            return 0
        if root.left is None and root.right is None:
            return 1
        if root.left is None or root.right is None:
            return max(self.run(root.left), self.run(root.right))+1
        return min(self.run(root.left), self.run(root.right))+1

sol = Solution()
print(sol.run(tree))