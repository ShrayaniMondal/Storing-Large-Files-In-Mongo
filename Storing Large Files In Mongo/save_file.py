# -*- coding: utf-8 -*-
"""
Created on Sat Oct 19 23:42:57 2019

@author: shrayani.mondal
"""
import pandas as pd
import uuid
import split_file
import save_data_chunks

def save_file(collection,filepath=None,data=None):    
    
    uniqueId = str(uuid.uuid4())
    if filepath:
        if filepath.endswith('.csv'):
            data_t = pd.read_csv(filepath,error_bad_lines=False,encoding= 'latin-1')
            if data_t.shape[0] == 0:
                return 'No data in the csv. Please upload with data'
            if data_t.shape[0] <= 20:
                return 'Number of records less than or equal to 20. Please upload file with more records'
        elif filepath.endswith('.xlsx'):
            data_t = pd.read_excel(filepath,encoding= 'latin-1')
            if data_t.shape[0] == 0:
                return 'No data in the excel. Please upload with data'
            if data_t.shape[0] <= 20:
                return 'Number of records less than or equal to 20. Please upload file with more records'
        else:
            return 'please upload correct file'
        #data_t.dropna(how='all', axis=1,inplace=True)     
    elif data is not None:
        data_t = data
        #data_t.dropna(how='all', axis=1,inplace=True)     
    
    columns = list(data_t.columns)
    chunks,filesize= split_file.split_file(data_t)        
    save_data_chunks.save_data_chunks(chunks,collection,uniqueId,columns)
    return uniqueId
