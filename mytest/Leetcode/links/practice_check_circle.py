from Leetcode.links.single_link import SingleLink, Node


def check_circle(link):
    slow = link.head
    fast = link.head
    while slow and fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False


def reverse(link):
    cur = link.head
    pre = None
    while cur:
        temp = cur.next
        cur.next = pre
        pre = cur
        cur = temp
    return pre


def merge_sort_link(l1, l2):
    l1head = l1.head
    l2head = l2.head
    node = Node(0)
    l3 = node
    while l1head and l2head:
        if l1head.item > l2head.item:
            l3.next = l2head
            l2head = l2head.next
        else:
            l3.next = l1head
            l1head = l1head.next
        l3 = l3.next
    if l1head:
        l3.next = l1head
    if l2head:
        l3.next = l2head
    return node


def find_middle(link):
    slow = link.head
    fast = link.head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow.item


def feibo(n):
    if n <= 0:
        return 1
    return (feibo(n - 1) + feibo(n - 2))


def k(l, lstack, rstack):
    p = {
        '{': '}',
        '(': ')',
        '[': ']',
    }
    k = list(l)
    for i in k:
        if i in p.keys():
            lstack.put(i)
        else:
            if p.get(lstack.top()) == i:
                lstack.pop()
            else:
                rstack.put(i)
    if lstack is None and rstack is None:
        return True
    else:
        return False


if __name__ == '__main__':
    for i in range(10):
        f = feibo(i)
        print(f, end=' ')

    l = '({[{]})'
