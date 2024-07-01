#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: saraelqaisi
"""

from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter(object):
    """CRUD operations for Animal collection in MongoDB """
    
    def __init__(self, USER, PASS):
        #check if user or password are empty
        if not USER or not PASS:
            print("Username & password cannot be empty.")
            return
        
        # Connection Variables
        HOST= 'nv-desktop-services.apporto.com'
        PORT= 31727
        DB= 'AAC'
        COL= 'animals'
        
        try:
            # Initialize Connection
            self.client = MongoClient('mongodb://%s:%s@%s:%d' % (USER,PASS,HOST,PORT))
            self.database = self.client['%s' % (DB)]
            self.collection = self.database['%s' % (COL)]
        
            #connection successful
            print("Connection Successful")
        except Exception as e:
            #exception if connection failed
            print(f"Connection failed: {str(e)}")
            raise
        
    # Create method
    def create(self, data):
        try:
            #if data received is not null or empty, try to insert data
            if data is not None and data:
                self.database.animals.insert_one(data) 
                return True
            else: 
                #data is None or empty, return false
                return False
        except Exception as e:
            #return exception
            print(f"Exception handler: error in creating document: {str(e)}")
   
    # Read method
    def read(self, data):
        try:
            #check if data is None or not
            if data is not None:
                #check if data is an empty dictionary
                if not data:
                    #empty, so return all documents
                    result = self.database.animals.find()
                else:
                    #use given data to locate document 
                    result = self.database.animals.find(data)
                
                #return results as a list
                return list(result)
            else:
                #data is None, return empty list
                return []
        except Exception as e:
            #return exception
            print(f"Exception handler: error in reading document: {str(e)}")
    
    # Update method
    def update(self, data, update_info):
        try:
            #if parameters are not null or empty, attempt an update 
            # & return number of modified objects
            if data is not None and update_info is not None and data and update_info:
                result = self.database.animals.update_many(data, update_info)
                return result.modified_count
            else:
                #data was not updated due to being None or empty, return 0
                return 0
        except Exception as e:
            print(f"Exception handling: error updating document: {str(e)}")
            
    # Delete method
    def delete(self, data):
        try:
            # if data is not None, attempt to delete data & 
            # return number of deleted objects
            if data is not None and data:
                result = self.database.animals.delete_many(data)
                return result.deleted_count
            else:
                #data was not deleted, return 0
                return 0
        except Exception as e:
            #return exception
            print(f"Exception handler: error deleting document: {str(e)}")
        
        
        
        
        
        
        
        
        
        
        
        
        
        