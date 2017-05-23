#-*- coding: utf-8 -*-
import sys
from scrapy.spider import Spider
from scrapy.selector import Selector
from news.items import BaiduNewsItem
class BaiduSpider(Spider):
    name = 'baidu'
    allowed_domains = ['news.baidu.com']

    start_urls = []

    def start_requests(self):

        number = 20
        for i in range(number):
            url = 'http://news.baidu.com/ns?word=' + "湖人" + '&pn=' + str(int(i) * 20) + '&cl=2&ct=1&tn=news&rn=20&ie=utf-8&bt=0&et=0'

            self.start_urls.append(url)

        for url in self.start_urls:
            yield self.make_requests_from_url(url)

    def parse(self, response):
        html = Selector(response)
        item = BaiduNewsItem()
        data = html.xpath('//div')
        for i in data  :
            a = 0
