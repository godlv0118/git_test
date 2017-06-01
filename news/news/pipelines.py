# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
import codecs
import MySQLdb
import sys

defaultencoding = 'utf-8'
if sys.getdefaultencoding() != defaultencoding:
    reload(sys)
    sys.setdefaultencoding(defaultencoding)
class NewsPipeline(object):
    def __init__(self):
        self.file = codecs.open('b.json',mode='w',encoding='utf-8')
    def process_item(self, item, spider):
        line = json.dumps(dict(item))  + '\n'
        self.file.write(line.decode("unicode_escape"))
        return item
    def Baidu_item(self,item,spider):
        pass

class BaiduPl(object):


    def __init__(self):
        self.conn = MySQLdb.connect(
            user = 'root',
            passwd = 'lzk961207',
            db = 'news',
            host = 'localhost',
            charset = 'utf8',
        )
        self.cursor = self.conn.cursor()

        #清空
        self.cursor.execute('truncate table Baidu_baidu;')

        self.conn.commit()

    def process_item(self,item,spider):


        try:
            value = (
                     item['title'].encode('utf-8'),
                     item['content'].encode('utf-8'),
                     item['where'].encode('utf-8'),
                     item['time'].encode('utf-8'),
                     item['url'].encode('utf-8'),
                     )

            self.cursor.execute('insert into Baidu_baidu values(null,%s,%s,%s,%s,%s);',value)
            self.conn.commit()
        except MySQLdb.Error ,e:
            print "Error %d: %s" % (e.args[0], e.args[1])
        return item