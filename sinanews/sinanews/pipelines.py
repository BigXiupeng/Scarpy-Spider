# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class SinanewsPipeline(object):
    def process_item(self, item, spider):
        news_url = item['news_url']
        filename = news_url[7:-6].replace('/','_') 
        filename += ".txt"

        with open(item['filename'] + '/' + filename, "w") as f:
            f.write(item["news_content"])

        return item
