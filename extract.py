# -*- coding: utf-8 -*-

import csv
import os

def extract(file, hang, lie):

    temp = []
    
    with open(file, 'r', encoding = 'UTF-8') as db01:
        reader = csv.reader(db01)
        for index, rows in enumerate(reader):
            if index >= hang-1:
                temp.append(rows[(lie-1):])
#            column = [row[] for row in reader]
#            print(column)
#    print(temp)
    out_name = 'Extrac_' + os.path.basename(file)

    with open('./output/' + out_name, 'w', encoding = 'UTF-8') as f:
        write = csv.writer(f, lineterminator = '\n')
        for row in temp:
            write.writerow(row)
        print(write)

# extract('Region1_output_L=4_overlap=6um.csv', 229, 2)
