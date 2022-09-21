'''
开篇问题：为什么工程中都喜欢用红黑树，而不是其他平衡二叉查找树呢？

平衡二叉树的严格定义：
    二叉树中任意一个节点的左右子树的高度相差不能大于1。从这个定义来看，完全二叉树、满二叉树其实都是平衡二叉树，但是非完全二叉树也有可能是平衡二叉树。
     例如：           13
               12          11
            10    9     8     7
          6      4 3
                    0
红黑树的英文是“Red-Black Tree”，简称 R-B Tree。它是一种不严格的平衡二叉查找树

红黑树中的节点，一类被标记为黑色，一类被标记为红色。除此之外，一棵红黑树还需要满足这样几个要求：[没理解]
    根节点是黑色的；
    每个叶子节点都是黑色的空节点（NIL），也就是说，叶子节点不存储数据；
    任何相邻的节点都不能同时为红色，也就是说，红色节点是被黑色节点隔开的；
    每个节点，从该节点到达其可达叶子节点的所有路径，都包含相同数目的黑色节点；

回答开篇问题：
    红黑树的插入、删除、查找各种操作性能都比较稳定。对于工程应用来说，要面对各种异常情况，为了支撑这种工业级的应用，
    我们更倾向于这种性能稳定的平衡二叉查找树。


红黑树理解起来太难，暂时放弃，有空了深入研究
'''