from scrapy import cmdline


cmdline.execute("scrapy crawl baidu ".split())
#cmdline.execute("scrapy crawl baidu -o b.json".split())