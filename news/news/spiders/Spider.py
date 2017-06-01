#-*- coding: utf-8 -*-

import sys

from scrapy.spiders import Spider
from scrapy.selector import Selector
from ..items import BaiduNewsItem
import re

defaultencoding = 'utf-8'
if sys.getdefaultencoding() != defaultencoding:
    reload(sys)
    sys.setdefaultencoding(defaultencoding)

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
        item = BaiduNewsItem()
        html = Selector(response)
        body = html.xpath('//*[@id="content_left"]')[0]

        #print html.xpath('//body').extract()
        #b = body.xpath('./child::*')
        results = body.xpath('div/div [@class = "result"]')  #获取每一小块新闻
        #c = d.xpath('./child::*')
        for result in results:

            title_xpath = result.xpath('h3 [@class = "c-title"]')

            url = title_xpath.xpath('a/@href').extract()[0]

            title = title_xpath.xpath('string(.)').extract()[0]

            other_xpath = result.xpath('div')

            if other_xpath.xpath('div[2]'):
                where_time = other_xpath.xpath('div[2]/p/text()').extract()
                content_xpath = other_xpath.xpath('div[2]')
                where, time, content = baidudetail(where_time,content_xpath)

            else:
                where_time = other_xpath.xpath('p/text()').extract()
                content_xpath = other_xpath
                where, time, content = baidudetail(where_time, content_xpath)


            item['title'] = title
            item['content'] = content
            item['where'] = where
            item['time'] = time
            item['url'] = url

            yield item

def baidudetail(where_time,content_xpath):
    where_time = where_time[0]
    list = where_time.split('\xc2\xa0\xc2\xa0')
    where = list[0]
    time = list[1]
    content = content_xpath.xpath('string(.)').extract()[0].encode('utf-8')
    content = content.replace(where_time, '')
    content = content.replace('百度快照', '')
    return where,time,content
