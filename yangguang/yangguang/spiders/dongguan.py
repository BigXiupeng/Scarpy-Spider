# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from yangguang.items import YangguangItem


class DongguanSpider(CrawlSpider):
    name = 'dongguan'
    allowed_domains = ['wz.sun0769.com']
    start_urls = ['http://wz.sun0769.com/index.php/question/questionType?type=4&page=0']

    rules = (
        Rule(LinkExtractor(allow=r'type=4'), follow = True),
        Rule(LinkExtractor(allow=r'question/\d+/\d+.shtml'), callback ="parse_item", follow = False),
    )
    def parse_item(self, response):
        print(response.url)
        item = YangguangItem()
        num = response.xpath('//div[@class="wzy1"]//td[2]/span[2]/text()').extract()
        if num:
            item['num'] = num[0].split(':')[-1]
        else:
            num = response.xpath('//div[@class="cleft"]/strong[@class="tgray14"]/text()').extract()[0].split(':')[-1]
        item['url'] = response.url
        name = response.xpath('//div[@class="wzy1"]//td[2]/span[1]/text()').extract()
        if name:
            item['name'] = name[0].split(":")[-1]
        else:
            item['name'] = response.xpath('//div[@class="cleft"]/strong[@class="tgray14"]/text()').extract()[0].split('\xa0\xa0')[0].split(':')[-1]
        content = response.xpath('//div[@class="contentext"]/text()').extract()
        if content:
            item['content'] = content[0].lstrip()
        else:
            item['content'] = response.xpath('//td[@class="txt16_3"]/text() | //div[@class="c1 text14_2"]/text()').extract()[0].lstrip()
        
        yield item

