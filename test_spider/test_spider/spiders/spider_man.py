import scrapy


class SpiderManSpider(scrapy.Spider):
    name = 'spider_man'

    def start_requests(self):
        urls = [
            'http://www.expoeast.com/ee16/public/Exhibitors.aspx?Index=All&sortMenu=118003'
        ]

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse_links)

    def parse_links(self, response):
        home_url = 'http://www.expoeast.com/ee16/public/'
        for link in response.xpath('//tr[@id="trnode"]/td/a').css('a.exhibitorName::attr(href)').extract():
            yield scrapy.Request(url=home_url+link, callback=self.parse_content)

    def parse_content(self, response):
        content = response.css('div.col-sm-8')
        yield {
            'name': content.css('h1::text').extract(),
            'city': content.css('span.BoothContactCity::text').extract(),
            'state': content.css('span.BoothContactState::text').extract(),
            'zip': content.css('span.BoothContactZip::text').extract(),
            'country': content.css('span.BoothContactCountry::text').extract(),

        }
