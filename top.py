# -*- coding: utf-8 -*-

import readfile
import extract

def top(path, f_type, hang, lie):

    f_list = readfile.readfile(path, f_type)

    for i in f_list:
        extract.extract(i, hang, lie)
    
    return


top('./raw/', '.csv', 229, 2)
