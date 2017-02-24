# -*- coding: utf-8 -*-
import scrapy


class AaoMajorsSpider(scrapy.Spider):
    name = "aao_majors"
    # allowed_domains = ["202.118.31.197"]
    start_urls = ['http://202.118.31.197/ACTIONQUERYCLASSSCHEDULE.APPPROCESS?filter=1']

    def parse(self, response):
        for item in response.xpath('//select[@name="MajorNO"]/option'):
            major_id = item.xpath('@value').extract_first()
            major_name = item.xpath('text()').extract_first()

            if major_id == '':
                continue
            if '\r' in major_id:
                major_id.replace('\r', '')
            # if '"' in major_id:
            #     major_id.replace('"', '')

            yield {
                'major_id': major_id,
                'major_name': major_name
            }
