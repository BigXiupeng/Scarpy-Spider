# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class XiaoshuoItem(scrapy.Item):
    # define the fields for your item here like:
    novel_name = scrapy.Field()
    novel_url = scrapy.Field()
    part_url = scrapy.Field()
    part_name = scrapy.Field()
    neirong = scrapy.Field()
    kind_name = scrapy.Field()
    file_novel = scrapy.Field()
    kind_url = scrapy.Field()
