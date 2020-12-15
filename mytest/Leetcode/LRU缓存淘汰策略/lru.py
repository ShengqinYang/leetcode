'''
应用场景：如何用实现 最近最少使用策略LRU 缓存淘汰策略呢？
leet code: 146
        运用你所掌握的数据结构，设计和实现一个  LRU (最近最少使用) 缓存机制。
        它应该支持以下操作： 获取数据 get 和 写入数据 put 。
        获取数据 get(key) - 如果密钥 (key) 存在于缓存中，则获取密钥的值（总是正数），否则返回 -1。
        写入数据 put(key, value) - 如果密钥不存在，则写入其数据值。
            当缓存容量达到上限时，它应该在写入新数据之前删除最近最少使用的数据值，从而为新的数据值留出空间
    哈希表+双向链表
    哈希表: 查询 O(1)
    双向链表: 有序, 增删操作 O(1)

LRU算法：缓存淘汰策略（最近最少使用，选择最近最久未使用的页面予以淘汰。）
思路：我们去维护一个有序单向链表，越靠近链表尾部的结点是越早之前访问的。当有一个新的数据被访问的时候，我们从头开始顺序遍历链表。
1）如果此数据之前已经被缓存在链表中了，我们遍历得到这个数据对应的结点，并将其从原来的位置删除，然后再插入到链表的头部。
2）如果此数据没有被缓存在链表中，又可以分为俩种情况：
3）如果此时缓存未满，则将此结点直接插入到链表的头部
4）如果此时缓存已满，则链表尾结点删除，将新的数据结点插入到链表的头部。
其他缓存算法：
FIFO--->先进先出      LFU---> 最少使用
'''


class DNode():

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache():
    '''
    哨兵节点,即为了解决边界问题而出现的
    '''

    def __init__(self, capacity):
        self.cap = capacity
        self.hkeys = {}  # 字典
        # self.top和self.tail作为哨兵节点, 避免越界
        self.top = DNode(None, -1)
        self.tail = DNode(None, -1)
        self.top.next = self.tail
        self.tail.prev = self.top

    def get(self, key):
        '''
        获取数据，表示最近用到，所以将数据置头
        :param key:
        :return:
        '''
        print(self.hkeys.keys())
        if key in self.hkeys.keys():  # 更新结点顺序
            print('sdsd')
            cur = self.hkeys[key]
            # 跳出原来的位置
            cur.next.prev = cur.prev
            cur.prev.next = cur.next

            # 最近用过的置于链表首部
            top_node = self.top.next
            self.top.next = cur
            cur.prev = self.top
            cur.next = top_node
            top_node.prev = cur
            return self.hkeys[key].value
        else:
            return -1

    def put(self, key, value):
        if key in self.hkeys.keys():
            cur = self.hkeys[key]
            cur.value = value
            # 跳出原来的位置
            cur.prev.next = cur.next
            cur.next.prev = cur.prev

            # 最近用过的置于链表首部
            top_node = self.top.next
            self.top.next = cur
            cur.prev = self.top
            cur.next = top_node
            top_node.prev = cur
        else:
            # 增加新节点到头部
            cur = DNode(key, value)
            self.hkeys[key] = cur
            # 最近用过的置于链表首部
            top_node = self.top.next
            self.top.next = cur
            cur.prev = self.top
            cur.next = top_node
            top_node.prev = cur
            if len(self.hkeys.keys()) > self.cap:
                self.hkeys.pop(self.tail.prev.key)
                # 去掉原来尾节点
                self.tail.prev.prev.next = self.tail
                self.tail.prev = self.tail.prev.prev

    def __repr__(self):
        vals = []
        p = self.top.next
        while p.next:
            vals.append(str(p.value))
            p = p.next
        return '->'.join(vals)


if __name__ == '__main__':
    cache = LRUCache(2)
    cache.put(1, 55)
    cache.put(2, 33)
    print(cache)
    cache.get(2)  # 返回  1
    # cache.put(3, 66)  # 该操作会使得密钥 2 作废
    # print(cache)
    # cache.get(2)  # 返回 -1 (未找到)
    # cache.put(4, 4)  # 该操作会使得密钥 1 作废
    # print(cache)
    # cache.get(1)  # 返回 -1 (未找到)
    # cache.get(3)  # 返回  3
    # print(cache)
    # cache.get(4)  # 返回  4
    # print(cache)
