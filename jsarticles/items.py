# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item,Field


class ArticlesItem(Item):

    url = Field()
    title = Field()
    author = Field()
    author_url = Field()
    reads = Field()
    comments = Field()
    likes = Field()
    rewards = Field()
