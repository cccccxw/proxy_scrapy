#!/usr/bin/python3
# -*- coding: utf-8 -*-



import pymongo
import requests
import os
import time

MONGO_URI = 'localhost'
MONGO_DB = 'proxy'
name = 'ProxyItem'


class get_from_db(object):
    def __init__(self,name):
        self.mongo_uri = MONGO_URI
        self.mongo_db = MONGO_DB
        self.name = name

    def open_db(self):
        self.client = pymongo.MongoClient(self.mongo_uri)
        self.db = self.client[self.mongo_db]

    
    def find_item(self):
        quary = {}
        count = self.db[self.name].count()
        if count <10:
            os.system("scrapy crawl proxies_wt")
            time.sleep(1)
            os.system("scrapy crawl proxies")
            time.sleep(1)
        responses = self.db[self.name].find(quary)
        self.db[self.name].delete_one(quary)
        try:
            return (responses[0]['ip'])
        except:
            return None



def get_one_proxy(name = name):
    r = get_from_db(name)
    r.open_db()
    return r.find_item()





if __name__ == '__main__':
    r = get_from_db()
    r.open_db()
    res = r.find_item()
    if check_proxy(res):
        print(res)
    else :
        get_one_proxy()
