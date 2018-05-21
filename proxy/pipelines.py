# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import re

import pymongo
from scrapy.exceptions import DropItem


class SpeedPipeline(object):
    def __init__(self):
        self.limit = 2.1

    def process_item(self, item, spider):
        if item['speed']:
            item['speed'] = float(re.findall(r"\d+\.?\d*",str(item['speed']))[0])
            if item['speed'] < self.limit:
                return item
            return DropItem('Drop a ip')

class MongoPipeline(object):
    def __init__(self,mongo_uri,mongo_db):
        self.mongo_uri = mongo_uri
        self.mongo_db = mongo_db

    @classmethod
    def from_crawler(cls,crawler):
        return cls(
            mongo_uri = crawler.settings.get('MONGO_URI'),
            mongo_db = crawler.settings.get('MONGO_DB')
        )

    def open_spider(self,spider):
        self.client = pymongo.MongoClient(self.mongo_uri)
        self.db = self.client[self.mongo_db]


    def process_item(self,item,spider):
        name = item.__class__.__name__
        try:
            ip = item['ip'] + ':' + item['port']
            self.db[name].remove({'ip' : ip})
            self.db[name].insert({'ip' : ip, 'speed' : item['speed']})
        except:
            pass
        return item

    def close_spider(self,spider):
        self.client.close()
