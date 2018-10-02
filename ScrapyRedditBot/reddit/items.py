# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

from scrapy import Item, Field

class RedditItem(scrapy.Item):

	title = scrapy.Field()
	img_link = scrapy.Field()
	img = scrapy.Field()
