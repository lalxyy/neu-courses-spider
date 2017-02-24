# -*- coding: utf-8 -*-
import scrapy


class AaoClassesSpider(scrapy.Spider):
    name = 'aao_classes'
    start_urls = ['http://202.118.31.197/ACTIONQUERYCLASSSCHEDULE.APPPROCESS?filter=1']

    def parse(self, response):
        for item in response.xpath('//select[@name="ClassNO"]/option'):
            class_id = item.xpath('@value').extract_first()
            class_name = item.xpath('text()').extract_first()
            if class_id == '':
                continue

            yield {
                'class_id': class_id,
                'class_name': class_name
            }
