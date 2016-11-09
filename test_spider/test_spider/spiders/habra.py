# coding: utf-8
import scrapy


class HabraSpider(scrapy.Spider):
    name = 'habra'

    def start_requests(self):
        urls = ['https://habrahabr.ru/company/carrotquest/blog/300396/']

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        data = response.css('strong::text').extract()
        for item in data:
            yield {
                'text': item
            }
