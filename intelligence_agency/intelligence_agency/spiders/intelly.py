import scrapy

class Spiderintelly(scrapy.Spider):
    name = 'intelly'
    start_urls =[
        'https://www.cia.gov/readingroom/historical-collections'
    ]
    custom_setting = {
        'FEED_URI': 'intelly.json',
        'FEED_FORMAT': 'json',
        'FEED_EXPORT_ENCODING': 'utf-8',
        'CONCURRENT_REQUEST': 24,
        'MEMUSAGE__LIMIT_MB': 2048,
        'MEMUSAGE_NOTIFY_MAIL': ['admin@mail.com'],
        'ROBOTSTXT_OBEY': True,
        'USERAGENT': 'intelly'
    }
    def parse(self, response):
        links_desclasified = response.xpath('//a[starts-with(@href,"collection")]/@href').getall()

        for link in links_desclasified:
            yield response.follow(link, callback=self.parse_link)


    def parse_link(self, response):
        pass
