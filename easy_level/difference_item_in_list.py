# coding=utf-8
'''
一个列表中有一个元素只出现一次，其他都出现两次
标准的解法是使用二进制异或运算, 异或运算有如下规律

a ^ a = 0
0 ^ a = a
满足交换律

a ^ b = b ^ a

所以在列表中每一个元素异或之后， 由交换律，有a^a^b^b^c^d^d = 0^c^0 = c
'''


def my_solution(inList):
    '''
    1. 自己的思路基本上是先排序，时间都花费在排序上
    2. 然后pop出前两个，如果不一致，就是那个单独出现一次的元素
    耗时是在排序上，排序之后就变成了[1, 1, 2, 2, 3, 3, 4, 5, 5,]
    然后pop出前两个对比是否相等
    '''
    sorted_list = sorted(inList)
    while sorted_list:
        first = sorted_list.pop(0)
        if not sorted_list:
            break
        second = sorted_list.pop(0)
        if first != second:
            break
    return first


def binary_solution(inList):
    '''
    标准解法
    '''
    tmp = 0
    for i in inList:
        tmp ^= i
    return tmp
