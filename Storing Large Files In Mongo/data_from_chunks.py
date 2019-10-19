# -*- coding: utf-8 -*-
"""
Created on Sat Oct 19 23:47:02 2019

@author: shrayani.mondal
"""
import open_dbconn
import pandas as pd
import json

def data_from_chunks(uniqueId,collection):
    dbconn,dbcollection = open_dbconn.open_dbconn(collection)
    
    data_json = dbcollection.find({"uniqueId" :uniqueId})
    
    count = data_json.collection.count_documents({"uniqueId" :uniqueId})
    
    data_t1 = pd.DataFrame()
    for counti in range(count):
        data_t = pd.DataFrame(json.loads(data_json[counti].get('InputData')))                        
        data_t1 = data_t1.append(data_t,ignore_index=True)
    
    dbconn.close()
    
    return data_t1 
