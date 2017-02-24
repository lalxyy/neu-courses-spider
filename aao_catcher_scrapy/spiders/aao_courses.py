# -*- coding: utf-8 -*-
import scrapy


class AaoCoursesSpider(scrapy.Spider):
    name = 'aao_courses'
    start_urls = ['http://202.118.31.197/ACTIONQUERYCLASSSCHEDULE.APPPROCESS']

    def parse(self, response):
        for class_selector in response.xpath('//select[@name="ClassNO"]/option'):
            class_id = class_selector.xpath('@value').extract_first()
            if class_id == '':
                continue
            for year_term_selector in response.xpath('//select[@name="YearTermNO"]/option'):
                year_term_id = year_term_selector.xpath('@value').extract_first()
                if year_term_id == '':
                    continue
                yield scrapy.http.FormRequest(
                    url='http://202.118.31.197/ACTIONQUERYCLASSSCHEDULE.APPPROCESS?mode=2&query=1',
                    callback=self.parse_class,
                    formdata={
                        'ClassNO': class_id,
                        'YearTermNO': year_term_id
                    },
                    dont_filter=True,
                    meta={
                        'class_id': class_id,
                        'year_term_id': year_term_id
                    }
                )

    def parse_class(self, response):
        class_id = response.meta['class_id']
        year_term_id = response.meta['year_term_id']
        for course_raw in response.xpath('//body/script/text()').extract():
            record = course_raw.strip()[16:-3].split('","')
            table_id = record[0][5:]
            weekday = int(table_id.split('#')[0])
            order_in_day = int(table_id.split('#')[1])
            task_id = record[1]
            course_name = record[2]
            teacher_name = record[3]
            week_type = record[5]
            classroom_name = record[6]
            # week parser
            for week in record[4].split('.'):
                weeks = []
                if '-' in week:
                    start_week = int(week.split('-')[0])
                    end_week = int(week.split('-')[1])
                    for x in range(start_week, end_week + 1):
                        weeks.append(x)
                else:
                    weeks.append(int(week))

                for w in weeks:
                    yield {
                        'class_id': class_id,
                        'year_term_id': year_term_id,
                        'weekday': weekday,
                        'order_in_day': order_in_day,
                        'task_id': task_id,
                        'course_name': course_name,
                        'teacher_name_from_courses': teacher_name,
                        'week': w,
                        'week_type': week_type,
                        'classroom_name': classroom_name
                    }
