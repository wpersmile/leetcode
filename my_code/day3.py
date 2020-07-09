#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2020/7/9 23:15
# @Author  : wperSmile
# @Subject : https://leetcode-cn.com/problems/palindrome-number/


# 字符串切片
def isPalindrome(x):
    if x < 0:
        return False
    x = str(x)
    x_len = len(x)
    if x_len == 1:
        return True
    mid = int(x_len / 2)
    if x[0:mid + 1:1] == x[-1:-(mid + 2):-1]:
        return True
    else:
        return False


# 数字反转
def isPalindrome2(x):
    if x < 0:
        return False
    x_copy = x
    rs = 0
    while x != 0:
        rs = rs * 10 + x % 10
        x = int(x / 10)
    if rs == x_copy:
        return True
    else:
        return False


if __name__ == '__main__':
    num = 1221
    print(isPalindrome2(num))
