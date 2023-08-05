import scrapy


class InbiziaSpider(scrapy.Spider):
    name = "inbizia"
    allowed_domains = ["www.inbizia.com"]
    start_urls = ["https://www.inbizia.com/forex/berita"]

    def parse(self, response):
        for news in response.css('div.col-8.lh-120'):
            urls = 'https://www.inbizia.com'
            yield {
                'Title':news.css('a.font-link::text').get(),
                'Link':urls+news.css('a.font-link::attr(href)').get()
            }



