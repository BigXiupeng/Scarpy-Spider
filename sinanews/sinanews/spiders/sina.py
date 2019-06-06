# -*- coding: utf-8 -*-
import scrapy
from sinanews.items import SinanewsItem 
import os

class SinaSpider(scrapy.Spider):
    name = 'sina'
    allowed_domains = ['sina.com.cn']
    start_urls = ['http://news.sina.com.cn/guide/']

    def parse(self, response):
        parent_title = response.xpath('//h3[@class="tit02"]/a/text()').extract()
        parent_url = response.xpath('//h3[@class="tit02"]/a/@href').extract()
        son_title = response.xpath('//ul[@class="list01"]//a/text()').extract()
        son_url = response.xpath('//ul[@class="list01"]//a/@href').extract()

        # 爬取所有大类
        for i in range(0,len(parent_title)):
                # 指定大类的目录名称
                parentFilename = "./sina" + parent_title[i]

                # 判断有没有这个目录，没有就创建
                if (not os.path.exists(parentFilename)):
                    os.makedirs(parentFilename)

                # 爬取所有小类
                for j in range(0, len(son_title)):
                    item = SinanewsItem()

                    item['parent_title'] = parent_title[i]
                    item['parent_url'] = parent_url[i]

                    #判断小类的url是否以大类的url开头，如果是返回True
                    if_belong = son_url[j].startswith(parent_url[i])
                    if if_belong:
                        son_filename = parentFilename + "/" + son_title[j]
                        if (not os.path.exists(son_filename)):
                            os.makedirs(son_filename)
                        item['son_title'] = son_title[j]
                        item['son_url'] = son_url[j]
                        item['filename'] = son_filename
                        yield scrapy.Request(url = item['son_url'], meta = {'meta_1':item}, callback = self.second_parse)

    def second_parse(self, response):
        item = response.meta['meta_1']

        news_url = response.xpath('//a/@href').extract()
        
        for i in range(0, len(news_url)):
            if_belong = news_url[i].startswith(item['parent_url']) and news_url[i].endswith('.shtml')

            if if_belong:
                item['news_url'] = news_url[i]
                item['filename'] = item['filename']
                yield scrapy.Request(url = item['news_url'], meta = {"meta_2" : item}, callback = self.detail_parse)

    def detail_parse(self, response):
        item = response.meta['meta_2']
        news_title = response.xpath('//h1[@class="main-title"]/text()').extract()
        news_content = response.xpath('//div[@class="article"]//text()').extract()        
        news_content = "".join(news_content).replace(' ','').replace('\n','')
        if news_title:
            item['news_title'] = news_title[0]
        else:
            item['news_title'] = "null"
        item['news_content'] = news_content

        yield item





