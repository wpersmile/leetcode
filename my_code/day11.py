#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2020/7/19 22:31
# @Author  : wperSmile
# @Subject : https://leetcode-cn.com/problems/climbing-stairs/


class Test:
    # 递归
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2
        return self.climbStairs(n - 1) + self.climbStairs(n - 2)

    # 动态规划
    def climbStairs2(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2
        dps = [-1] * (n + 1)
        dps[1] = 1
        dps[2] = 2
        i = 3
        while i <= n:
            dps[i] = dps[i - 1] + dps[i - 2]
            i = i + 1
        return dps[n]


t = Test()
test_n = 1
print(t.climbStairs2(test_n))
