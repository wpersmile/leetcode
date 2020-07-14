#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2020/7/14 22:25
# @Author  : wperSmile
# @Subject : https://leetcode-cn.com/problems/remove-element/


def removeElement(nums, val):
    list_len = len(nums)
    i = 0
    while i < list_len:
        if list_len == 0:
            break
        if nums[i] == val:
            nums.pop(i)
            if i != 0:
                i = i - 1
            list_len = list_len - 1
            continue
        i = i + 1
    return nums


if __name__ == '__main__':
    test_num = [2, 2, 2, 2]
    test_val = 2
    print(removeElement(test_num, test_val))
