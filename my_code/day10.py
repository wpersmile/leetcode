#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2020/7/16 23:54
# @Author  : wperSmile
# @Subject : https://leetcode-cn.com/problems/intersection-of-two-linked-lists/submissions/


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        headA_len = 0
        headB_len = 0

        if headA == None or headB == None:
            return None

        p = headA
        while p != None:
            p = p.next
            headA_len = headA_len + 1

        p = headB
        while p != None:
            p = p.next
            headB_len = headB_len + 1

        value = 0
        if headA_len >= headB_len:
            value = headA_len - headB_len
            pa = headA
            pb = headB
            for i in range(0, value):
                pa = pa.next
            while pa.next != None:
                if pa != pb:
                    pa = pa.next
                    pb = pb.next
                else:
                    return pa
            if pa == pb:
                return pa
        else:
            value = headB_len - headA_len
            pa = headA
            pb = headB
            for i in range(0, value):
                pb = pb.next
            while pa.next != None:
                if pa != pb:
                    pa = pa.next
                    pb = pb.next
                else:
                    return pa
            if pa.next == None:
                if pa == pb:
                    return pa
        return None
