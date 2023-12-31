from time import sleep
import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

from crawler_news.spiders import LibertyTimes
from crawler_news.spiders import ebc
from crawler_news.spiders import udn
from crawler_news.spiders import EtToday

settings = get_project_settings()
process = CrawlerProcess(settings)

print('start')

for spider_name in process.spiders.list():
    if spider_name != 'localhost':
        print ("Running spider %s" % (spider_name))
        process.crawl(spider_name)


process.start() # the script will block here until all crawling jobs are finished

print('done')
