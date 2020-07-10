#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2020/7/10 22:34
# @Author  : wperSmile
# @Subject : https://leetcode-cn.com/problems/longest-common-prefix/


def longestCommonPrefix(strs):
    s_len = len(strs)
    s_prefix = ""
    if s_len == 0:
        return s_prefix
    s_compare = strs[0]
    for i in range(1, len(s_compare) + 1):
        for j in range(0, s_len):
            if s_compare[:i:1] != strs[j][:i:1]:
                s_prefix = s_compare[:i - 1:1]
                return s_prefix
        s_prefix = s_compare[:i:1]
    return s_prefix


if __name__ == '__main__':
    test_strs = ["abcd", "abc", "ab"]
    print(longestCommonPrefix(test_strs))
