# -*- coding: utf-8 -*-
"""
Created on Sat Jul 28 11:35:19 2018

@author: sylar
"""

import numpy as np

X = np.loadtxt("spectre011.csv", delimiter=",")
L = []
D = []

for i in range(len(X)-1):
    if(i <= len(X)-3):
        if((X[i]==X[i+1]).all()):
            if((X[i]==X[i+2]).all()):
                L.append(i+1)
                L.append(i+2)
                L.append(i+3)
            else:
                continue

for i in L:
    D.append(X[i-1])

out = np.array(D)
print(out.shape)

np.savetxt('test.csv', out, fmt='%.8e', delimiter = ',')