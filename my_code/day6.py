#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2020/7/12 22:02
# @Author  : wperSmile
# @Subject : https://leetcode-cn.com/problems/search-insert-position/


def searchInsert(nums, target):
    if target in nums:
        return nums.index(target)
    for index, num in enumerate(nums):
        if target > num:
            continue
        elif target <= num:
            return index
    return len(nums)


if __name__ == '__main__':
    test_nums = [1, 3, 5, 6, 7, 9]
    test_target = 3
    print(searchInsert(test_nums, test_target))
