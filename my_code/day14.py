# -*- encoding: utf-8 -*-
"""
@File    : day14.py
@Time    : 2021/5/5 17:02
@Author  : WPER_SMILE
@Info    : count_prime
"""

import time


def count_prime_num(num):
    count = 0
    for i in range(2, num + 1):
        flag = False
        for j in range(2, i):
            if i % j == 0:
                flag = True
        if not flag:
            count = count + 1
    return count


def count_prime_num2(num):
    count = 0
    for i in range(2, num + 1):
        count = count + (1 if is_prime(i) else 0)
    return count


def is_prime(num):
    for i in range(2, num):
        if i * i <= num:
            if num % i == 0:
                return False
    return True


def count_prime_num3(num):
    count = 0
    eliminate = []
    for i in range(2, num + 1):
        for j in range(2, num):
            if i * i <= num:
                if i * j > num:
                    break
                else:
                    eliminate.append(i * j)
    for i in range(2, num + 1):
        if i in eliminate:
            continue
        else:
            count = count + (1 if is_prime(i) else 0)
    return count


def count_prime_num4(num):
    prime = [True] * num
    count = 0
    for i in range(2, num + 1):
        if prime[i - 1]:
            count = count + 1
            for j in range(i, num):
                if j * i <= num:
                    prime[j * i - 1] = False
                else:
                    break
    return count


star = time.time()
print(count_prime_num(50_000))
end = time.time()
spend_time = end - star
print(spend_time)

star = time.time()
print(count_prime_num2(50_000))
end = time.time()
spend_time = end - star
print(spend_time)

star = time.time()
print(count_prime_num3(50_000))
end = time.time()
spend_time = end - star
print(spend_time)

star = time.time()
print(count_prime_num4(50_000))
end = time.time()
spend_time = end - star
print(spend_time)
