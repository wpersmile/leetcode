#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2020/7/8 22:49
# @Author  : wperSmile
# @Subject : https://leetcode-cn.com/problems/reverse-integer/


def reverse(x):
    max_num = 2 ** 31 - 1
    min_num = -2 ** 31
    flag = 1
    rs = 0
    if x < 0:
        flag = -1
        x = -x
    while x != 0:
        rs = rs * 10 + x % 10
        x = int(x / 10)
    if rs > max_num or rs < min_num:
        return 0
    else:
        if flag == 1:
            return rs
        else:
            return -rs


if __name__ == '__main__':
    num = 123456
    print(reverse(num))
