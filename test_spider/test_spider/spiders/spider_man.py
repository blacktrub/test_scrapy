import scrapy


class SpiderManSpider(scrapy.Spider):
    name = 'spider_man'

    def start_requests(self):
        urls = [
            'http://www.expoeast.com/ee16/public/Exhibitors.aspx?Index=All&sortMenu=118003'
        ]

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        for link in response.xpath('//tr[@id="trnode"]/td/a').css('a.exhibitorName::attr(href)').extract():
            yield {'link': link}
