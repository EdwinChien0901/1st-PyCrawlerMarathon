# -*- coding: utf-8 -*-
import scrapy
import time
from myproject.items import MyprojectItem

class PttcrawlerSpider(scrapy.Spider):
    name = 'PTTCrawler'
    allowed_domains = ['www.ptt.cc']
    start_urls = ['https://www.ptt.cc/bbs/Gossiping/index.html']
        
    def start_requests(self):
        for i in range(10):
            time.sleep(2)
            url = "https://www.ptt.cc/bbs/Gossiping/index" + str(38809 - i) + ".html"
            yield scrapy.Request(url, callback=self.parse, cookies={"over18":"1"})
   
    def parse(self, response):
        item = MyprojectItem()
        target = response.css("div.r-ent")
      
        for tag in target:
            try:
                item['title'] = tag.css("div.title a::text")[0].extract()
                item['author'] = tag.css('div.author::text')[0].extract()
                item['date'] = tag.css('div.date::text')[0].extract()
                item['push'] = tag.css('span::text')[0].extract()
                item['url'] = tag.css('div.title a::attr(href)')[0].extract()

                yield item

            except IndexError:
                pass
                continue