#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author: wangwenjie
@contact: xidianw3@163.com
@file: beta.py
@time: 2018/1/22 下午7:27
@desc: beta分布图像

"""

import sys

import pymc
from scipy.stats import beta
import matplotlib.pyplot as plt
import numpy as np
reload(sys)
sys.setdefaultencoding('utf8')


a, b = 32, 199

print pymc.rbeta(1 + a, b)
print pymc.rbeta(1 + a, b)
print pymc.rbeta(1 + a, b)
print pymc.rbeta(1 + a, b + 1)
print pymc.rbeta(1 + a, b + 1)
print pymc.rbeta(1 + a, b + 1)


mean, var, skew, kurt = beta.stats(a, b, moments='mvsk')
print beta.pdf(0.1, a, b)
x = np.linspace(0, 1, 100)
plt.plot(x, beta.pdf(x, a, b), 'r-', lw=5, alpha=0.6, label='beta pdf')
plt.show()
