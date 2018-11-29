# -*- coding: utf-8 -*-

import os

def readfile(path, ex):
    
    dirs = os.listdir(path)
    f_list = []
    
    for i in dirs:
        if os.path.splitext(i)[1] == ex:
            # print(path + i)
            f_list.append(path + i)
    
    return f_list

# readfile("./raw/", ".csv")
