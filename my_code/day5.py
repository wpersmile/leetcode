#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2020/7/11 20:49
# @Author  : wperSmile
# @Subject : https://leetcode-cn.com/problems/valid-parentheses/


def isValid(s):
    s_len = len(s)
    s_list = list(s)
    if s_len % 2 != 0:
        return False
    index_list = []
    for i in range(0, s_len):
        if s_list[i] == '{' or s_list[i] == '[' or s_list[i] == '(':
            index_list.append(s_list[i])
            continue
        if len(index_list) == 0:
            continue
        if s_list[i] == '}' or s_list[i] == ']' or s_list[i] == ')':
            if s_list[i] == '}':
                if '{' != index_list.pop():
                    return False
            elif s_list[i] == ']':
                if '[' != index_list.pop():
                    return False
            else:
                if '(' != index_list.pop():
                    return False
    if len(index_list) != 0:
        return False
    else:
        return True


if __name__ == '__main__':
    s = '{}[]{[]}()'
    print(isValid(s))
