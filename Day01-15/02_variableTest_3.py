#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
使用input()函数获取键盘输入(字符串)
使用int()函数将输入的字符串转换成整数
使用print()函数输出带占位符的字符串
"""
a = int(input('a = '))
b = int(input('b = '))

print('%d + %d = %d' % (a, b, a + b))  # 加
print('%d - %d = %d' % (a, b, a - b))  # 减
print('%d * %d = %d' % (a, b, a * b))  # 乘
print('%d / %d = %f' % (a, b, a / b))  # 除
print('%d // %d = %d' % (a, b, a // b))  # 取商
print('%d %% %d = %d' % (a, b, a % b))  # 取余
print('%d ** %d = %d' % (a, b, a ** b))  # a的b次方

