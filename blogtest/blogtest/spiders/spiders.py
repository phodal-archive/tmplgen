from scrapy import Request
import csv

try:
    from scrapy.spider import Spider
except:
    from scrapy.spider import BaseSpider as Spider
from scrapy.contrib.spiders import CrawlSpider

class blogSpider(CrawlSpider):
    name = "blog"
    allowed_domains = ["localhost"]

    def start_requests(self):
        listings = []
        with open('blogtest/spiders/100k.csv', 'rb') as csvfile:
            spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
            for row in spamreader:
                print row[0]
                listings.append(row[0])
        print listings
        for i in listings:
            print i
            yield Request('http://localhost:8080/immobile-%s' % i,
                    callback=self.parse)

    def parse(self, response):
        filename = "files/" + response.url.split("/")[-1] + '.html'
        with open(filename, 'wb') as f:
            f.write(response.body)
