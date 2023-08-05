import scrapy


class InbiziaSpider(scrapy.Spider):
    name = "inbizia"
    allowed_domains = ["www.inbizia.com"]
    start_urls = ["https://www.inbizia.com/forex/berita?s=1"]

    def parse(self, response):
        urls = 'https://www.inbizia.com'
        for news in response.css('div.col-8.lh-120'):
            yield {
                'Title':news.css('a.font-link::text').get(),
                'Link':urls+news.css('a.font-link::attr(href)').get()
            }

        next_page = urls + response.css('a.page-link::attr(href)')[5].get()
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)




