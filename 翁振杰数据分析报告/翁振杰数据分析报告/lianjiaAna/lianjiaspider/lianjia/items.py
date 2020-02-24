# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class LianjiaItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    id = scrapy.Field()  # 编号
    area=scrapy.Field()#区域
    adress=scrapy.Field()#地址
    community = scrapy.Field()  # 小区
    shelf_time = scrapy.Field()#上架时间
    rent = scrapy.Field()#租金
    # rent_type = scrapy.Field()#租用方式
    house_type = scrapy.Field()#户型
    square = scrapy.Field()#面积
    towards = scrapy.Field()#朝向
    floor=scrapy.Field()#楼层
    describe = scrapy.Field()#介绍
    subway = scrapy.Field()#地铁信息
    img_url = scrapy.Field()  # 图片链接
    url=scrapy.Field()
    download_time = scrapy.Field()#采集时间

