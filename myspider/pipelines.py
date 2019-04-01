# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json

from pymongo import MongoClient


class PrintPipeLine(object):
    def process_item(self, item, spider):
        print('from print pipeline', item)

class DyPipeLineMongo(object):

    def open_spider(self, spider):
        if spider.name == 'douyu':
            print('start spider')
            con = MongoClient(host='127.0.0.1', port=27017) # 实例化mongoclient
            db = con['admin']
            db.authenticate('python', 'python')
            self.connection = con.douyu.live


    def close_spider(self, spider):
        if spider.name == 'douyu':
            print('close spider')

    def process_item(self, item, spider):
        print('pipelines item ------>', item)
        self.connection.insert(item)
        return item

class DyPipeLine(object):

    def open_spider(self, spider):
        if spider.name == 'douyu':
            print('start spider')
            self.f = open('douyu.txt', 'a')

    def close_spider(self, spider):
        if spider.name == 'douyu':
            print('close spider')
            self.f.close()

    def process_item(self, item, spider):
        # print('pipelines item ------>', item)
        self.f.write(json.dumps(item) + '\n')
        return item


