#!/usr/bin/python3
# -*- coding: utf-8 -*-

import pymongo
import requests

mongo_uri = 'localhost'
mongo_db = 'proxy'
name = 'ValueProxy'

class ValueProxy(object):
    def __init__(self,value_proxies):
        self.mongo_uri = mongo_uri
        self.mongo_db = mongo_db
        self.name = name
        self.value = value_proxies



    def open_db(self):
        self.client = pymongo.MongoClient(self.mongo_uri)
        self.db = self.client[self.mongo_db]


    def insert_item(self):

        self.db[name].remove({'ip' : self.value})

        self.db[name].insert({'ip' : self.value})
        

    def find_item(self):
        quary = {}
        return self.db[name].count(quary)

def value_proxy(value_proxies):
    if value_proxies:
        r = ValueProxy(value_proxies)
        r.open_db()
        r.insert_item()
        return
    else:
        r = ValueProxy(value_proxies)
        r.open_db()
        return r.find_item()

if __name__ == '__main__':
    print(value_proxy('10.206.25.104:808'))

        
