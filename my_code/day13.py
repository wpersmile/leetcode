# -*- encoding: utf-8 -*-
"""
@File    : day13.py
@Time    : 2021/5/2 17:25
@Author  : WPER_SMILE
@Info    : reverse list
"""


class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None

    def get_value(self):
        return self.value


class SingleList:
    def __init__(self):
        self.__head = None

    def get_head(self):
        return self.__head

    def is_empty(self):
        return self.__head is None

    def length(self):
        if self.is_empty():
            return 0
        curr = self.__head
        count = 1
        while curr.next is not None:
            curr = curr.next
            count = count + 1
        return count

    def append(self, value):
        if self.is_empty():
            self.__head = Node(value)
        else:
            t = self.__head
            while t is not None:
                if t.next is None:
                    t.next = Node(value)
                    break
                else:
                    t = t.next

    def travel(self):
        t = self.__head
        while t is not None:
            print(t.value)
            t = t.next

    def reverse_by_iteration(self):
        curr_node = self.__head
        prev_node = None
        while curr_node is not None:
            next_node = curr_node.next
            curr_node.next = prev_node
            prev_node = curr_node
            curr_node = next_node
        self.__head = prev_node

    def reverse_by_recursion(self):
        head = self.__head
        self.__head = self.recursion(head)

    def recursion(self, head):
        if head is None or head.next is None:
            return head
        new_head = self.recursion(head.next)
        head.next.next = head
        head.next = None
        return new_head


if __name__ == '__main__':
    sig = SingleList()
    sig.append('10')
    sig.append('11')
    sig.append('12')
    sig.append('13')
    sig.append('14')
    sig.append('15')
    sig.append('16')

    print(sig.length())
    sig.travel()
    sig.reverse_by_recursion()
    sig.travel()
