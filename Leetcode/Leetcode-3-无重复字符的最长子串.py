'''
无重复字符的最长子串
题目：给定一个字符串，找出其中不含有重复字符的最长子串长度。
    示例 1:
        输入:"abcabcbb"
        输出:3
        解释:因为无重复字符的最长子串是 "abc"，所以其长度为 3。
    示例 2:
        输入:"bbbbb"
        输出:1
        解释:因为无重复字符的最长子串是 "b"，所以其长度为 1。
    示例 3:
        输入:"pwwkew"
        输出:3
        解释:因为无重复字符的最长子串是 "wke"，所以其长度为 3。
'''


def mymain(mystr):
    if not mystr:
        return None
    newlist = list(mystr)
    # print(set(newlist), len(newlist))
    return len(set(newlist))


if __name__ == '__main__':
    mystr = "abcabcbb"
    result = mymain(mystr)
    print(result)
