# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class NewsItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass
class BaiduNewsItem(scrapy.Item):
    title = scrapy.Field()      #新闻的标题
    content = scrapy.Field()    #新闻的大概内容
    where = scrapy.Field()      #新闻的出处
    time = scrapy.Field()       #新闻发布时间
    url = scrapy.Field()        #新闻的链接

