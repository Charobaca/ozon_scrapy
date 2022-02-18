import scrapy


class OzonSpiderSpider(scrapy.Spider):
    name = 'ozon_spider'
    allowed_domains = ['https://www.ozon.ru']
    start_urls = ['https://www.ozon.ru/']

    def parse(self, response):
        pass
