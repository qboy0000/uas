# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class UasItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    agent_type = scrapy.Field()
    agent_name = scrapy.Field()
    agent_version = scrapy.Field()
    os_type = scrapy.Field()
    os_name = scrapy.Field()
    os_versionName = scrapy.Field()
    os_versionNumber = scrapy.Field()
    os_producer = scrapy.Field()
    os_producerURL = scrapy.Field()
    linux_distibution = scrapy.Field()
    agent_language = scrapy.Field()
    agent_languageTag = scrapy.Field()
    uas = scrapy.Field()
    uas_id = scrapy.Field()


