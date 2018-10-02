# -*- coding: utf-8 -*-
import scrapy

from scrapy.spiders import CrawlSpider
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

from reddit.items import RedditItem

class PictureSpider(CrawlSpider):
    name = 'picture'
    allowed_domains = ['www.reddit.com']
    start_urls = ['http://www.reddit.com/']

    # Next page links:
    # https://www.reddit.com/r/pics/?count=25&after=t3_6y7v9e
    # https://www.reddit.com/r/pics/?count=50&after=t3_6yb047
    # Creating regexp based on links:
    # r'/?count=\d+&after=\w*'

    rules = [
        Rule(LinkExtractor(allow=[r'/?count=\d+&after=\w*']),
            callback='parse_item',
    		follow = True)


    ]

    def parse_item(self, response):
        # For debugging:
        # print(response.url)

        # In Chrome, right click on image -> Inspect
        # In Inspect area right click on element and Copy - XPath
        # //*[@id="thing_t3_6ye9u6"]/div[2]/div[1]/p[1]/a

    	divs = response.css('div.thing')

    	for div in divs:

    		item = RedditItem()

    		item['title'] = div.xpath('div[2]/div[1]/p[1]/a/text()').extract()
    		item['img_link'] = div.xpath('div[2]/div[1]/p[1]/a/@href').extract()

    		yield item

            # For debugging:
    		# title = div.xpath('div[2]/div[1]/p[1]/a/text()').extract()
    		# img_link = div.xpath('div[2]/div[1]/p[1]/a/@href').extract()
            #
            #
    		# print title
    		# print img_link
