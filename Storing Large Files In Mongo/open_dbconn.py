# -*- coding: utf-8 -*-
"""
Created on Sat Oct 19 23:37:12 2019

@author: shrayani.mondal
"""
from pymongo import MongoClient

def open_dbconn(collection):
    try: 
        conn = MongoClient('localhost', 27017)
        print("Connected successfully!!!") 
    except:   
        print("Could not connect to MongoDB") 
    
    db = conn.PythonExperiments
    
    db_IngestedData = db[collection]
    
    return conn,db_IngestedData