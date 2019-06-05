# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
import pymongo

class XiaoshuoPipeline(object):
    def __init__(self):
        client = pymongo.MongoClient(host='localhost', port=27017)
        self.db = client['spider']
        self.coll = self.db['novel']
        #self.db.authenticate('jamesjiajia', 'python')

    def process_item(self, item, spider):
        #filename = item['file_novel']
        #part_name = item['part_name']
        #content = part_name + '\n' + item['neirong'] + '\n'
        #with open(filename, 'a', encoding='utf-8') as f:
        #    f.write(content)
        post_item = dict(item)
        self.coll.insert(post_item)
        return item
