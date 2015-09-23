from scrapy import Request

try:
    from scrapy.spider import Spider
except:
    from scrapy.spider import BaseSpider as Spider
from scrapy.contrib.spiders import CrawlSpider


class blogSpider(CrawlSpider):
    name = "blog"
    allowed_domains = ["localhost"]

    def start_requests(self):
        for i in range(0, 500):
            yield Request('http://127.0.0.1:8000/api/app/blog_detail/%d' % i,
                    callback=self.parse)

    def parse(self, response):
        filename = "files/" + response.url.split("/")[-1] + '.html'
        with open(filename, 'wb') as f:
            f.write(response.body)
