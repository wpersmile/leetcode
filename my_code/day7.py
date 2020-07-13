#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2020/7/13 22:58
# @Author  : wperSmile
# @Subject : https://leetcode-cn.com/problems/remove-duplicates-from-sorted-array/


# 逻辑常规判断
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


# 链表实现
def lengthOfLastWord2(s):
    s_list = list(s)
    last_word_list = []
    while len(s_list) != 0:
        s_pop = s_list.pop()
        if s_pop != ' ':
            last_word_list.insert(0, s_pop)
        else:
            if len(last_word_list) != 0:
                break
    last_word = ''.join(last_word_list)
    return len(last_word)


if __name__ == '__main__':
    test_s = ' 33   2  '
    print(lengthOfLastWord2(test_s))
