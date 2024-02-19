import math


class Solution:
    def findMedianSortedArrays_1(self, nums1, nums2):
        '''归并排序思路合并两个有序数组
        第一步：找出合并后有序数组的中间所有位置
        第二步：两个数组合并成一个有序数组
        第三步：找出中位数
        '''
        len1 = len(nums1)
        len2 = len(nums2)
        m = (len1 + len2) / 2

        if not (len1 + len2) % 2:  # 找出合并后有序数组的中间所有位置
            left_index, right_index = int(m) - 1, int(m)
        else:
            left_index, right_index = math.floor(m), math.floor(m)  # 找出合并后有序数组的中间所有位置

        p, q = 0, 0
        count = -1
        new_nums = []
        while p < len(nums1) and q < len(nums2):
            if nums2[q] > nums1[p]:
                new_nums.append(nums1[p])
                p += 1
            else:
                new_nums.append(nums2[q])
                q += 1
            count += 1
            if count == right_index:
                break
        print(new_nums)
        new_nums = new_nums + nums1[p:] + nums2[q:]
        print(new_nums)
        return (new_nums[right_index] + new_nums[left_index]) / 2


    def findMedianSortedArrays_2(self, nums1, nums2):
        """
        将两个正序数组进行归并排序， 然后寻找归并后的数组中的中位数

        :param nums1:
        :param nums2:
        :return:
        """
        big_nums = []
        while nums1 or nums2:
            if nums1:
                t1 = nums1[0]
            else:
                big_nums.extend(nums2)
                break
            if nums2:
                t2 = nums2[0]
            else:
                big_nums.extend(nums1)
                break
            if t1 < t2:
                big_nums.append(nums1.pop(0))
            else:
                big_nums.append(nums2.pop(0))

        length = len(big_nums)
        if length % 2:
            median = big_nums[length // 2]
        else:
            median = (big_nums[length // 2] + big_nums[(length - 1) // 2]) / 2

        return median


if __name__ == '__main__':
    nums1 = [0, 1, 3, 4, 5]
    nums2 = [-2, 1, 3, 6, 7, 8]
    result = Solution().findMedianSortedArrays_1(nums1, nums2)
    print(result)
    result = Solution().findMedianSortedArrays_2(nums1, nums2)
    print(result)
