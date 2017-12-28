# -*- coding: utf-8 -*-
from scrapy.spider import CrawlSpider,Rule,Request
from scrapy.linkextractors import LinkExtractor
from bbjh_spider.items import BbjhSpiderItem

class BbjhSpider(CrawlSpider):
    name = 'bbjh'
    item = BbjhSpiderItem()

    rules = (
        Rule(LinkExtractor(allow='\.html', restrict_xpaths='//a[@href]'), callback='parse_item', follow=True),
    )

    def __init__(self, url='www.bbjhart.com', *args, **kwargs):
        super(BbjhSpider, self).__init__(*args, **kwargs)
        self.item['name'] = url
        self.start_urls = ['http://' + url]
        self.allowed_domains = [url]

    def parse_item(self, response):
        self.item['url'] = response.url
        yield self.item
