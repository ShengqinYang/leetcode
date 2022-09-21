'''
题目：
    给定两个大小为m和n的有序数组nums1和nums2。
    请你找出这两个有序数组的中位数，并且要求算法的时间复杂度为O(log(m + n))。
    你可以假设nums1和nums2不会同时为空。
示例 1:
    nums1 = [1, 3]
    nums2 = [2]
    则中位数是 2.0
示例 2:
    nums1 = [1, 2]
    nums2 = [3, 4]
    则中位数是 (2 + 3)/2 = 2.5
'''
import math


class Myclass():
    def __init__(self, nums1, nums2):
        self.nums1 = nums1
        self.nums2 = nums2

    @property
    def middlenums(self):
        nums = sorted(self.nums1 + self.nums2)
        lenght = len(nums)
        if lenght == 1:
            return nums[0]
        if lenght % 2:
            middlen = math.floor(len(nums) / 2)
            return nums[middlen]
        else:
            n = int(len(nums) / 2)
            middlen = (nums[n - 1] + nums[n]) / 2
            return middlen


if __name__ == '__main__':
    nums1 = []
    nums2 = [3]
    myclass = Myclass(nums1, nums2)
    print(myclass.middlenums)
