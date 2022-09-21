'''

前序遍历的递推公式：
preOrder(r) = print r->preOrder(r->left)->preOrder(r->right)

中序遍历的递推公式：
inOrder(r) = inOrder(r->left)->print r->inOrder(r->right)

后序遍历的递推公式：
postOrder(r) = postOrder(r->left)->postOrder(r->right)->print r
'''

class TreeNode():
    '''树节点'''

    def __init__(self, item):
        self.item = item
        self.left = None
        self.right = None


def pre_travel(tree):
    if tree:
        yield tree.item
        yield from pre_travel(tree.left)
        yield from pre_travel(tree.right)


def in_travel(tree):
    if tree:
        yield from in_travel(tree.left)
        yield tree.item
        yield from in_travel(tree.right)


def post_travel(tree):
    if tree:
        yield from post_travel(tree.left)
        yield from post_travel(tree.right)
        yield tree.item


if __name__ == '__main__':
    '''
    构造2叉树:
            china
        省          直辖市
    四川   河北   北京    重庆
    '''

    n1 = TreeNode('china')

    n2 = TreeNode('省')
    n3 = TreeNode('直辖市')

    n4 = TreeNode('四川')
    n5 = TreeNode('河北')
    n6 = TreeNode('北京')
    n7 = TreeNode('重庆')

    n1.left, n1.right = n2, n3
    n2.left, n2.right = n4, n5
    n3.left, n3.right = n6, n7

    print(list(pre_travel(n1)))
    print(list(in_travel(n1)))
    print(list(post_travel(n1)))
