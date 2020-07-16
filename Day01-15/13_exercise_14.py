# -*- coding: utf-8 -*-
"""
例子2：使用多进程对复杂任务进行“分而治之”,单线程演示
完成1~100000000求和的计算密集型任务
"""
from time import time


def main():
    total = 0
    number_list = [x for x in range(1, 100000001)]
    start = time()
    for number in number_list:
        total += number
    print(total)
    end = time()
    print('Execution time: %.3fs' % (end - start))


if __name__ == '__main__':
    main()