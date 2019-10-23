# -*- coding: utf-8 -*-
import scrapy


class QuotesSpiderSpider(scrapy.Spider):
    name = 'quotes_spider'
    start_urls = ['http://quotes.toscrape.com/']

    def parse(self, response):
        quotes = response.xpath('//div[@class="quote"]')
        for quote in quotes:
            text = quote.xpath('.//span[@class="text"]/text()').extract_first()
            author = quote.xpath('.//span/small[@class="author"]/text()').extract_first()
            tags = quote.xpath('.//meta[@class="keywords"]/@content').extract_first()

            # next_page_url = response.xpath('//ul/li[@class="next"]/a/@href').extract_first()
            # if next_page_url:
            #     next_page_url = response.urljoin(next_page_url)
            #     yield scrapy.Request(next_page_url,callback=self.parse)

            author_page_url = quote.xpath('.//span/a[contains(text(),"about")]/@href').extract_first()
            author_page_url = response.urljoin(author_page_url)

            yield scrapy.Request(author_page_url,callback=self.parse_author,meta={
                'text':text,
                'author':author,
                'tags':tags
            })
        next_page_url = response.xpath('//ul/li[@class="next"]/a/@href').extract_first()
        if next_page_url:
            next_page_url = response.urljoin(next_page_url)
            yield scrapy.Request(next_page_url,callback=self.parse)

    def parse_author(self,response):
        author_detail = response.xpath('//div[@class="author-details"]')
        author_date_of_birth = author_detail.xpath('.//span[@class="author-born-date"]/text()').extract_first()
        author_birth_place = author_detail.xpath('.//span[@class="author-born-location"]/text()').extract_first()
        text = response.meta['text']
        author = response.meta['author']
        tags = response.meta['tags']

        yield {
            'text':text,
            'tags':tags,
            'author':author,
            'author_date_of_birth':author_date_of_birth,
            'author_birth_place':author_birth_place
        }
