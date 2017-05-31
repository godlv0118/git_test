#-*- coding: utf-8 -*-
import sys
import scrapy
from scrapy.http import Request
from scrapy.spider import Spider
from scrapy.selector import Selector
from ..items import BaiduNewsItem
class BaiduSpider(Spider):
    name = 'baidu'
    allowed_domains = ['news.baidu.com']

    start_urls = []
    user_agent = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36"
    headers = {'User-Agent': user_agent}
    def start_requests(self):

        number = 20
        for i in range(number):
            url = 'http://news.baidu.com/ns?word=' + "湖人" + '&pn=' + str(int(i) * 20) + '&cl=2&ct=1&tn=news&rn=20&ie=utf-8&bt=0&et=0'

            self.start_urls.append(url)

        for url in self.start_urls:
            yield self.make_requests_from_url(url)
            #yield scrapy.Request(url,callback=self.parse,headers=self.headers)

    def parse(self, response):
        print response.body
        html = Selector(response)
        item = BaiduNewsItem()
        data = html.xpath('//div')
        for i in data  :
            a = 0
