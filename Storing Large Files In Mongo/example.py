# -*- coding: utf-8 -*-
"""
Created on Sat Oct 19 23:48:46 2019

@author: shrayani.mondal
"""
import save_file
import data_from_chunks
import pandas as pd

#collection name and filepath
collection = "test"
filepath = "Change_Data_sample.csv"

#get the size of the original data
data_og = pd.read_csv(filepath,error_bad_lines=False,encoding= 'latin-1')
size_og = data_og.size

#save the data in mongo
uniqueId = save_file.save_file(collection,filepath)

#fetch the data back from mongo
data = data_from_chunks.data_from_chunks(uniqueId,collection)
size_fetched = data.size

#Check the size of the data
if(size_og == size_fetched):
    print("Hurray!")
else:
    print("Booo!")