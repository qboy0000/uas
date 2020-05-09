# -*- coding: utf-8 -*-
# @author:''
# @filename:$Title.py

import scrapy
# from uas.items import UasItem
from ..items import UasItem
import requests
import json


class UasSpider(scrapy.Spider):
    name = 'uas'
    allowed_domains = ["useragentstring.com"]

    def start_requests(self):
        print("start_requests==>")
        return [scrapy.FormRequest("http://useragentstring.com/pages/useragentstring.php",
                                   callback=self.parse_list)]

    def parse_list(self, response):
        print("parse_list==>", response)
        uas_menu_weblist = response.xpath('//a[@class="unterMenuName"]/@href').extract()
        for web in uas_menu_weblist:
            print("parse_list==>", web)
            yield scrapy.Request(url="http://useragentstring.com{}".format(web), callback=self.parseItem)

    def parseItem(self, response):
        uas_list = response.xpath('//div[@id="liste"]//ul//a')
        for uas in uas_list:
            uas_text = uas.xpath('text()').extract_first()
            uas_href = uas.xpath('@href').extract_first()
            if "user agents strings -->>" in uas_text:
                yield scrapy.Request(url="http://useragentstring.com{}".format(uas_href), callback=self.parseItem)
            else:
                try:
                    uas_id = uas_href.split('id=')[1]

                    url = "http://useragentstring.com/?uas={}&getJSON=all".format(uas_text)
                    payload = {}
                    headers = {}
                    response = requests.request("GET", url, headers=headers, data=payload)
                    uas_json = json.loads(response.text.encode('utf8'))
                    if uas_json is not None:
                        uas_item = UasItem()
                        for k in uas_json.keys():
                            uas_item[str(k)] = uas_json[k]
                        uas_item['uas'] = uas_text
                        uas_item['uas_id'] = int(uas_id)
                        yield uas_item
                except Exception as ex:
                    print(ex)
                    with open('error.txt', 'a+') as err:
                        err.write(uas_text)
                        err.write('\n')
