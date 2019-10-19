# -*- coding: utf-8 -*-
"""
Created on Sat Oct 19 23:38:54 2019

@author: shrayani.mondal
"""
import math
import sys
import numpy as np    

def split_file(data): 
    data = data.reset_index(drop=True)          
    t_filesize  = (sys.getsizeof(data)/ 1024) / 1024               
    nulls = data.isnull().sum(axis=1)    
    null_index = nulls.idxmin()
    row1size = (sys.getsizeof(data.iloc[[null_index]]) / 1024) / 1024        
    capacity = 2
    nrows = data.shape[0]    
    if t_filesize > capacity:               
        if row1size != 0: rows = math.ceil(capacity / row1size )
        if rows != 0: 
            chunks = np.split(data,range(1 * rows, (nrows // rows + 1) * rows, rows))    
    elif t_filesize <= capacity:    
        chunks = []
        chunks.append(data)
    return chunks,t_filesize
