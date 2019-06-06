# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class SinanewsItem(scrapy.Item):
    # define the fields for your item here like:
    parent_title = scrapy.Field()
    son_title = scrapy.Field()
    
    parent_url = scrapy.Field()
    son_url = scrapy.Field()

    news_url = scrapy.Field()
    news_title = scrapy.Field()
    news_content = scrapy.Field()
    filename = scrapy.Field()
