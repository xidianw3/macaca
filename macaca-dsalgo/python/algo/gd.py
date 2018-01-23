#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author: wangwenjie
@contact: xidianw3@163.com
@file: gd.py
@time: 2017/11/30 上午9:52
@desc: 梯度下降的一些基础算法

"""
import random
import sys

import numpy as np

reload(sys)
sys.setdefaultencoding('utf8')


def batch_gradient_descent(x, y, theta, alpha, m, max_iter):
    """
    批量梯度下降
    :param x: 
    :param y: 
    :param theta: 
    :param alpha: 
    :param m: 
    :param max_iter: 
    :return: 
    """
    x_trains = x.transpose()
    for i in range(0, max_iter):
        hypothesis = np.dot(x, theta)
        loss = hypothesis - y
        print 'iter=%d, loss=%s' % (i, str(loss))
        gradient = np.dot(x_trains, loss) / m
        theta = theta - alpha * gradient

    return theta


def stochastic_gradient_descent(x, y, theta, alpha, m, max_iter):
    """
    随机梯度下降
    :param x: 
    :param y: 
    :param theta: 
    :param alpha: 
    :param m: 
    :param max_iter: 
    :return: 
    """

    for i in range(0, max_iter):
        hypothesis = np.dot(x, theta)
        loss = hypothesis - y
        select_index = random.randint(0, m - 1)
        gradient = loss[select_index] * x[select_index]

        print 'iter=%d, select_index=%d, loss=%s' % (i, select_index, str(loss))
        theta = theta - alpha * gradient

    return theta


def predict(x, theta):
    m, n = np.shape(x)
    x_text = np.ones((m, n + 1))
    x_text[:, :-1] = x
    res = np.dot(x_text, theta)

    return res


if __name__ == '__main__':
    train_data = np.array([[1.1, 1.5, 1], [1.3, 1.9, 1],
                           [1.5, 2.3, 1], [1.7, 2.7, 1],
                           [1.9, 3.1, 1], [2.1, 3.5, 1],
                           [2.3, 3.9, 1], [2.5, 4.3, 1],
                           [2.7, 4.7, 1], [2.9, 5.1, 1]])

    train_label = np.array([2.5, 3.2, 3.9, 4.6, 5.3, 6, 6.7, 7.4, 8.1, 8.8])

    x_test = np.array([[3.1, 5.5], [3.3, 5.9], [3.5, 6.3], [3.7, 6.7], [3.9, 7.1]])
    y_test = np.array([9.5, 10.2, 10.9, 11.6, 12.3])

    m, n = np.shape(train_data)
    theta = np.ones(n)
    alpha = 0.1
    max_iter = 3

    theta = batch_gradient_descent(train_data, train_label, theta, alpha, m, max_iter)
    print 'theta=', theta

    res = predict(x_test, theta)
    print 'bgd res=', res

    theta = np.ones(n)
    theta = stochastic_gradient_descent(train_data, train_label, theta, alpha, m, max_iter)
    print 'theta=', theta

    ret = predict(x_test, theta)
    print 'sgd res=', res
