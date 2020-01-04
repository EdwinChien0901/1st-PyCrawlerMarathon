import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings


def main():
    target_urls = [
        'https://www.ptt.cc/bbs/Gossiping/M.1578144483.A.B71.html',
        'https://www.ptt.cc/bbs/Gossiping/M.1578144678.A.112.html'
    ]
    process = CrawlerProcess(get_project_settings())
    #給完整檔名(含副檔名)
    #process.crawl('PTTCrawler', start_urls=target_urls, filename='Ptt_Gossiping.json')
    #不給檔名,由close_spider處理
    #process.crawl('PTTCrawler', start_urls=target_urls)
    #只給檔名(沒有副檔名)
    process.crawl('PTTCrawler', start_urls=target_urls, filename='Gossiping')
    process.start()

if __name__ == '__main__':
    main()
