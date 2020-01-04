import scrapy
import time
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings


def main():
    #target_board = ['Gossiping', 'Stock']
    target_board = ['Tech_Job', 'Stock']
    process = CrawlerProcess(get_project_settings())
    #for board in target_board:
        #print("board : ", board)
    process.crawl('PTTCrawler', boards=target_board)
    process.start()
        #time.sleep(2)

if __name__ == '__main__':
    main()
