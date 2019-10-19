# -*- coding: utf-8 -*-
"""
Created on Sat Oct 19 23:45:31 2019

@author: shrayani.mondal
"""
import uuid
from datetime import datetime
import open_dbconn

def save_data_chunks(chunks,collection,uniqueId,columns):      
    dbconn,dbcollection = open_dbconn.open_dbconn(collection)
  
    for chi in range(len(chunks)):
        Id=str(uuid.uuid4())
        data_json = chunks[chi].to_json(orient='records',date_format='iso', date_unit='s')   
        
        dbcollection.insert_one({"uniqueId":uniqueId,
                                 "sNo":Id,
                                 "InputData":data_json,
                                 "ColumnsList":columns,
                                 "CreatedOn":str(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
                                 })
        print(chi)
        #breakpoint()
            
    dbconn.close()