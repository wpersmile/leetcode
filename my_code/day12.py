#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2020/7/20 23:08
# @Author  : wperSmile
# @Subject : https://leetcode-cn.com/problems/unique-paths/


# 动态规划
def uniquePaths(m: int, n: int) -> int:
    fs = [[0 for i in range(m)] for j in range(n)]
    for i in range(0, n):
        for j in range(0, m):
            if i == 0 or j == 0:
                fs[i][j] = 1
            else:
                fs[i][j] = fs[i - 1][j] + fs[i][j - 1]
    return fs[n - 1][m - 1]


if __name__ == '__main__':
    test_m = 7
    test_n = 3
    print(uniquePaths(test_m, test_n))
