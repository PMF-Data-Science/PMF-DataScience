import scrapy

with open('coins.txt') as file:
    data = file.read().split(',')

list_coins=[coin for coin in data]

class ScrapeTableSpider(scrapy.Spider):
    name = 'spider1'
 
    def start_requests(self):
        urls = [
            'https://www.coingecko.com/en/coins/{}'.format(coin) for coin in list_coins
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)
 
    def parse(self, response):
        yield {'m_c dominance' : response.xpath('//*[@class="tw-text-gray-900 dark:tw-text-white tw-font-medium"]//text()')[6].extract()}
        