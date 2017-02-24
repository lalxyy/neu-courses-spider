# -*- coding: utf-8 -*-
import scrapy


class AaoYearTermsSpider(scrapy.Spider):
    name = 'aao_year_terms'
    start_urls = ['http://202.118.31.197/ACTIONQUERYCLASSSCHEDULE.APPPROCESS?filter=1']

    def parse(self, response):
        for item in response.xpath('//select[@name="YearTermNO"]/option'):
            year_term_id = item.xpath('@value').extract_first()
            year_term_name = item.xpath('text()').extract_first()
            if year_term_id == '':
                continue

            yield {
                'year_term_id': year_term_id,
                'year_term_name': year_term_name
            }
