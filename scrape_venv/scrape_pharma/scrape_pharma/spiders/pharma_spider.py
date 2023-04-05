import scrapy

class pharama_spider(scrapy.Spider):
    name = 'myspider'
    start_urls = ['www.abbvie.com']

    def parse(self, response):
        le = LinkExtractor()
        for link in le.extract_links(response):
            url_lnk = link.url
            print (url_lnk)
