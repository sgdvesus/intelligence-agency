import scrapy
import os
os.remove('intelly.json')
class SpiderIntelly(scrapy.Spider):
    name = 'intelly'
    start_urls = [
        'https://www.cia.gov/readingroom/historical-collections'
    ]
    custom_settings = {
        'FEED_URI': 'intelly.json',
        'FEED_FORMAT': 'json',
        'FEED_EXPORT_ENCODING': 'utf-8',
        #'CONCURRENT_REQUEST': 24,
        #'MEMUSAGE__LIMIT_MB': 2048,
        #'MEMUSAGE_NOTIFY_MAIL': ['admin@mail.com'],
        'ROBOTSTXT_OBEY': True,
        'USER_AGENT': 'intelly'
    }
    def parse(self, response):
        links_desclasified = response.xpath('//a[starts-with(@href,"collection")]/@href').getall()

        for link in links_desclasified:
            yield response.follow(link, callback=self.parse_link, cb_kwargs={'url': response.urljoin(link)})


    def parse_link(self, response, **kwargs):
        link = kwargs['url']
        title = response.xpath('//h1[@class="documentFirstHeading"]/text()').get()
        paragraph = response.xpath('//div[@class="field-item even"]//p[not(@class) and not(strong)]/text()').get()
        #response.xpath('//div[@class="field-item even"]/p[3]/text()').get()
        #paragraph = response.xpath('//div[@class="field-item even"]/p[not(@child)]/text()').get()

        yield {
            'link': link,
            'title': title,
            'paragraph': paragraph
        }
