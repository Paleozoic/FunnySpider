from scrapy import cmdline

cmd_str = 'scrapy crawl zhihu'
cmdline.execute(cmd_str.split(' '))
