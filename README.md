# 东大班级课表爬虫

一只班级课表爬虫. 



需要安装 Scrapy. 

```shell
pip install scrapy

# Or use Anaconda (Recommended)
conda install -c conda-forge scrapy=1.3.2
```

使用方式:

```shell
cd aao-catcher-scrapy/spiders
scrapy runspider aao_courses.py -o ../out/aao_courses.csv
```



## Spiders

-   aao_classes.py: 教务系统中的所有班级

-   aao_courses.py: 课程

-   aao_departments.py: 学院列表

-   aao_majors.py: 专业列表

-   aao_relations.py: 学院-专业-班级的关系表 (参考关系数据库的一对多存储)

    ​

## 已知问题

-   没有充分利用 Scrapy 提供的项目组织结构
-   没有反爬虫处理 (实际操作中, 教务网站并没有做反爬虫)
-   没有后续分析