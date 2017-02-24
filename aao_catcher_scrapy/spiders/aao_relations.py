# -*- coding: utf-8 -*-
import scrapy


class AaoRelationsSpider(scrapy.Spider):
    name = 'aao_relations'
    url = 'http://202.118.31.197/ACTIONQUERYCLASSSCHEDULE.APPPROCESS'

    def start_requests(self):
        yield scrapy.Request(url=self.url)

    def parse(self, response):
        for department_selector in response.xpath('//select[@name="DeptNO"]/option'):
            dep_id = department_selector.xpath('@value').extract_first()
            if dep_id == '':
                continue
            yield scrapy.http.FormRequest(
                url=self.url,
                callback=self.parse_major,
                formdata={
                    'DeptNO': dep_id
                },
                dont_filter=True,
                meta={
                    'dep_id': dep_id
                }
            )

    def parse_major(self, response):
        dep_id = response.meta['dep_id']
        # print(response.body)
        for major_selector in response.xpath('//select[@name="MajorNO"]/option'):
            major_id = major_selector.xpath('@value').extract_first()
            if major_id == '':
                continue
            yield scrapy.http.FormRequest(
                url=self.url,
                callback=self.parse_come_year,
                formdata={
                    'DeptNO': dep_id,
                    'MajorNO': major_id
                },
                dont_filter=True,
                meta={
                    'dep_id': dep_id,
                    'major_id': major_id
                }
            )

    def parse_come_year(self, response):
        dep_id = response.meta['dep_id']
        major_id = response.meta['major_id']
        for come_year_selector in response.xpath('//select[@name="ComeYear"]/option'):
            come_year_id = come_year_selector.xpath('@value').extract_first()
            if come_year_id == '':
                continue
            yield scrapy.http.FormRequest(
                url=self.url,
                callback=self.parse_class,
                formdata={
                    'DeptNO': dep_id,
                    'MajorNO': major_id,
                    'ComeYear': come_year_id
                },
                dont_filter=True,
                meta={
                    'dep_id': dep_id,
                    'major_id': major_id,
                    'come_year_id': come_year_id
                }
            )

    def parse_class(self, response):
        dep_id = response.meta['dep_id']
        major_id = response.meta['major_id']
        come_year_id = response.meta['come_year_id']
        for class_selector in response.xpath('//select[@name="ClassNO"]/option'):
            class_id = class_selector.xpath('@value').extract_first()
            if class_id == '':
                continue
            yield {
                'dep_id': dep_id,
                'major_id': major_id,
                'come_year_id': come_year_id,
                'class_id': class_id
            }
