import re

from scrapy import Request

try:
    from scrapy.spider import Spider
except:
    from scrapy.spider import BaseSpider as Spider
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor as sle


class blogSpider(CrawlSpider):
    name = "blog"
    allowed_domains = ["dmoz.org"]
    start_urls = [
        "http://127.0.0.1:8000/api/app/blog_detail/",
    ]
    max_cid = 500

    def start_requests(self):
        for i in range(self.max_cid):
            yield Request('http://127.0.0.1:8000/api/app/blog_detail/%d' % i,
                    callback=self.parse)

    def parse(self, response):
        filename = response.url.split("/")[-2] + '.html'
        with open(filename, 'wb') as f:
            f.write(response.body)
