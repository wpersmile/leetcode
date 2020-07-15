#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2020/7/15 23:02
# @Author  : wperSmile
# @Subject : https://leetcode-cn.com/problems/plus-one/

def plusOne(digits):
    temps = []
    digits_len = len(digits)
    overflow = False
    first_pop = True
    while digits_len != 0:
        digits_len = digits_len - 1
        pop_num = digits.pop()
        if first_pop:
            pop_num = pop_num + 1
            first_pop = False
        if overflow:
            pop_num = pop_num + 1
        if pop_num == 10:
            temps.append(0)
            overflow = True
        else:
            temps.append(pop_num)
            overflow = False
    if overflow:
        temps.append(1)
    for i in range(0, len(temps)):
        digits.append(temps.pop())
    return digits


if __name__ == '__main__':
    nums = [1, 2, 9]
    print(plusOne(nums))
