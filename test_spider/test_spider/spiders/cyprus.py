import scrapy


class CyprusSpider(scrapy.Spider):
    name = 'cyprus'

    def start_requests(self):
        urls = [
            'http://www.cyprus.com/results.html?search=jewellery&sort=by-site-rank&page=9',
        ]

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse_links)

    def parse_links(self, response):
        home_url = 'http://www.cyprus.com/'
        for link in response.css('li div.popular_content div.restaurant_name h2 a::attr(href)').extract():
            yield scrapy.Request(url=home_url + link, callback=self.parse_content)

    def parse_content(self, response):
        yield {
            'name': response.css('div.profile_info h1 a::text').extract(),
            'address': ', '.join(response.xpath('//span[@id="company_address"]').css('span::text').extract()),
            'phone': None,
        }

    def get_phone(self):
        pass
