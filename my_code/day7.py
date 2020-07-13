#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2020/7/13 22:58
# @Author  : wperSmile
# @Subject : https://leetcode-cn.com/problems/remove-duplicates-from-sorted-array/


def lengthOfLastWord(s):
    s = s.rstrip()
    s_len = len(s)
    last_word = ''
    for i in range(0, s_len):
        if s[i] == ' ':
            last_word = ''
            continue
        else:
            last_word = last_word + s[i]
    return len(last_word)


if __name__ == '__main__':
    test_s = ' 2    33'
    print(lengthOfLastWord(test_s))
