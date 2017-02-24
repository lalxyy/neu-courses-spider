# -*- coding: utf-8 -*-
import scrapy


class AaoSpider(scrapy.Spider):
    name = "aao"
    # allowed_domains = ["aao.neu.edu.cn"]
    start_urls = ['http://202.118.31.197/ACTIONQUERYCLASSSCHEDULE.APPPROCESS?filter=1']

    def parse(self, response):
        for item in response.xpath('//select[@name="DeptNO"]/option'):
            dep_id = item.xpath('@value').extract_first()
            dep_name = item.xpath('text()').extract_first()
            if dep_id == '':
                continue

            yield {
                'dep_id': dep_id,
                'dep_name': dep_name
            }
