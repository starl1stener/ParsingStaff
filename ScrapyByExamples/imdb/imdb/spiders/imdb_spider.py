# -*- coding: utf-8 -*-
import scrapy


class ImdbSpiderSpider(scrapy.Spider):
    name = 'imdb_spider'
    allowed_domains = ['imdb.com']
    start_urls = ['http://imdb.com/chart/top']

    def parse(self, response):
        movies = response.xpath('//td[@class="titleColumn"]')
        for movie in movies:
        	title = movie.xpath('.//a/text()').extract_first()
        	rating = movie.xpath('.//following-sibling::td[contains(@class,"ratingColumn")]/strong/text()').extract_first()

        	yield {
                'title':title,
                'rating':rating
            }

