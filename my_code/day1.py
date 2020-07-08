#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2020/7/8 22:43
# @Author  : wperSmile
# @Subject : https://leetcode-cn.com/problems/two-sum/


# 暴力破解
def two_sum(nums, target):
    for i in range(0, len(nums) - 1):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return i, j
    return ()


# 哈希表
def two_sum2(nums, target):
    hash_map = {}
    for index1, num in enumerate(nums):
        index2 = hash_map.get(target - num)
        if index2 is not None and index1 != index2:
            return index1, index2
        hash_map[num] = index1
    return ()


if __name__ == '__main__':
    test_nums = (10, 3, 5, 4, 1, 8)
    print(two_sum(test_nums, 9))
    print(two_sum2(test_nums, 9))
