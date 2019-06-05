# -*- coding: utf-8 -*-
import scrapy
import os
from xiaoshuo.items import XiaoshuoItem


class NovelSpider(scrapy.Spider):
    name = 'novel'
    allowed_domains = ['530p.com']
    start_urls = ['http://www.530p.com']

    def parse(self, response):
        kind_urls = response.xpath("//div[@class='menu']/ul/li/a/@href").extract()[1:8]
        kind_names = response.xpath("//div[@class='menu']/ul/li/a/span/text()").extract()[1:8]
        items = []
        for each in range(len(kind_names)):
            if not os.path.exists(kind_names[each]):
                os.makedirs(kind_names[each])
                for offset in range(1,11):
                    item = XiaoshuoItem()
                    item['kind_name'] = kind_names[each]
                    item['kind_url'] = kind_urls[each] + str(offset) + '.htm'
                    items.append(item)
        for item in items:
            yield scrapy.Request(item['kind_url'], meta={'meta': item}, callback=self.parse_second)
        # for kind_name, kind_url in zip(kind_names, kind_urls):
        #    for offset in range(1,11):
        #        item = XiaoshuoItem()
        #        item['kind_name'] = kind_name
        #        item['kind_url'] = kind_url + offset + '.htm'
        #        if not os.path.exists(kind_name):
        #            os.makedirs(kind_name)
        #        items.append(item)
        # for item in items:
        #    yield scrapy.Request(item['kind_url'], meta={'meta': item}, callback=self.parse_second)

    def parse_second(self, response):
        meta = response.meta['meta']
        items = []
        novel_urls = response.xpath("//li[@class='conter1']/a/@href").extract()
        novel_names = response.xpath("//li[@class='conter1']/a/text()").extract()
        for novel_url, novel_name in zip(novel_urls, novel_names):
            item = XiaoshuoItem()
            novel_url = 'http://www.530p.com' + novel_url
            file_novel = meta['kind_name'] + '\\' + novel_name + '.txt'
            item['kind_name'] = meta['kind_name']
            item['kind_url'] = meta['kind_url']
            item['novel_name'] = novel_name
            item['novel_url'] = novel_url
            item['file_novel'] = file_novel
            items.append(item)
        for item in items:
            yield scrapy.Request(item['novel_url'], meta={'meta1': item}, callback=self.parse_third)
        #if self.offset < 10:
         #   self.offset += 1
          #  page_url = item['kind_url'] + str(self.offset) + '.htm'
           # yield scrapy.Request(page_url, callback=self.parse_second)

    def parse_third(self, response):
        meta1 = response.meta['meta1']
        items = []
        part_urls = response.xpath("//div[@class='clc']/a/@href").extract()[::-1]  # 章节url
        part_names = response.xpath("//div[@class='clc']/a/text()").extract()[::-1]  # 章节名字
        for part_url, part_name in zip(part_urls, part_names):
            item = XiaoshuoItem()
            part_url = 'http://www.530p.com' + part_url
            item['kind_name'] = meta1['kind_name']
            item['kind_url'] = meta1['kind_url']
            item['novel_name'] = meta1['novel_name']
            item['novel_url'] = meta1['novel_url']
            item['file_novel'] = meta1['file_novel']
            item['part_url'] = part_url
            item['part_name'] = part_name
            items.append(item)
        for item in items:
            yield scrapy.Request(item['part_url'], meta={'meta2': item}, callback=self.parse_forth)

    def parse_forth(self, response):
        item = response.meta['meta2']
        cp_neirong = response.xpath("//h1/text()|//div[@id='cp_content']/text()").extract()[0:-1]
        cps_title = cp_neirong[0] + '\n'
        cp_content = "\n".join(cp_neirong[1:]).strip()
        neirong = cps_title + cp_content
        item['neirong'] = neirong
        yield item

