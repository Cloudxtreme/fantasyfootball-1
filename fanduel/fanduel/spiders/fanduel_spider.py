import scrapy
from fanduel.items import FanduelItem

class FanduelSpider(scrapy.Spider):
	name = 'fanduel'
	allowed_domains = ['fanduel.com']
	start_urls = ['https://www.fanduel.com/e/Game/10791']

	def parse(self, response):
		for sel in response.xpath('//tbody/tr[@data-role="player"]'):
			item = FanduelItem()
			item['name'] = sel.xpath('td[@class="player-name"]/div/text()').extract()
			item['position'] = sel.xpath('td[@class="player-position"]/text()').extract()
			item['fppg'] = sel.xpath('td[@class="player-fppg"]/text()').extract()
			item['salary'] = sel.xpath('td[@class="player-salary"]/text()').extract()
			yield item
			
