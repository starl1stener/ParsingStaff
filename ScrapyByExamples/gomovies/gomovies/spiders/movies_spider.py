# -*- coding: utf-8 -*-
import scrapy


class MoviesSpiderSpider(scrapy.Spider):
    name = 'movies_spider'
    start_urls = ['https://gomovies.sc/movies/']

    def parse(self, response):
        contents = response.xpath('//div[@class="ml-item"]')
        for content in contents:
            url = content.xpath('.//a/@href').extract_first()
            title = content.xpath('.//span[@class="mli-info"]/h2/text()').extract_first()
            quality = content.xpath('//span[@class="mli-quality"]/text()').extract_first()

            yield {
                'title':title,
                'quality':quality,
                'url':url
            }

            next_page_url = response.xpath('//a[contains(text(),"Next ")]/@href').extract_first()
            if next_page_url:
                yield scrapy.Request(next_page_url,callback=self.parse)
