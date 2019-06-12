# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json

class YangguangPipeline(object):
    def __init__(self):
        self.file = open("minyi.json", "w")
    def process_item(self, item, spider):
        context = json.dumps(dict(item), ensure_ascii=False) + '\n'
        self.file.write(context)
        return item
    def spider_close(self, spider):
        self.file.close()
