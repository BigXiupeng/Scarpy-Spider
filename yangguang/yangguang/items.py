# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class YangguangItem(scrapy.Item):
    # define the fields for your item here like:
    num = scrapy.Field()
    url = scrapy.Field()
    name = scrapy.Field()
    content = scrapy.Field()


