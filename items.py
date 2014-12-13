import scrapy

class DoubanItem(scrapy.Item):
	title = scrapy.Field()
	author = scrapy.Field()
	# publisher = scrapy.Field()
	# year = year.Field()
	price = scrapy.Field()
	desc = scrapy.Field()
