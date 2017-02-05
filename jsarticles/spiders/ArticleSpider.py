#encoding = utf-8

from scrapy.spiders import CrawlSpider
from scrapy.http import Request, FormRequest
from scrapy.selector import Selector

from jsarticles.items import ArticlesItem


import json
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

import sys

reload(sys)
sys.setdefaultencoding('utf-8')

class ArticleSpider(CrawlSpider):

    name = 'articles'
    start_urls=[
        'http://www.jianshu.com/trending/monthly'
    ]

    def parse(self, response):

        item = ArticlesItem()

        selector = Selector(response)

        url = str(response.url)


        infos = selector.xpath('//ul[@class="note-list"]/li')


        for info in infos:

            author = info.xpath('div/div[1]/div/a/text()').extract()[0]

            author_url =info.xpath('div/div[1]/div/a/@href').extract()[0]
            title = info.xpath('div/a/text()').extract()[0]
            url = info.xpath('div/a/@href').extract()[0]

            reads = info.xpath('div/div[2]/a[1]/text()').extract()[1]
            comments = info.xpath('div/div[2]/a[2]/text()').extract()[1]

            likes = info.xpath('div/div[2]/span[1]/text()').extract()[0]
            rewards = info.xpath('div/div[2]/span[2]/text()').extract()

            if rewards:
                rewards = rewards[0]
            else:
                rewards = 0

            item['author'] = author
            item['author_url'] = 'http://www.jianshu.com'+author_url
            item['title'] = title
            item['url'] = 'http://www.jianshu.com'+url
            item['reads'] =reads
            item['comments'] = comments
            item['likes'] = likes
            item['rewards'] = rewards

            yield item


            for i in range(2,11):
                next_url = 'http://www.jianshu.com/trending/monthly?page=%s'%i
                yield Request(next_url,callback=self.parse)










