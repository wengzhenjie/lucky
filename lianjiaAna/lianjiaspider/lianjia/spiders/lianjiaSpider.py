# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request
from lianjia.items import LianjiaItem
import re
import datetime
import copy
#构造初始链接
def get_start_urls():
    base_url='https://sh.lianjia.com/zufang/'
    start='erp3000/#contentList'
    end='brp3000/#contentList'
    start_url=['brp'+str(i)+'erp'+str(i+500)+'/#contentList' for i in range(3000,25000,500)]
    start_url.append(start)
    start_url.append(end)
    urls=[]
    for i in start_url:
        for j in range(1,101):
            url=base_url+'pg'+str(j)+i
            urls.append(url)
    return urls

class LianjiaspiderSpider(scrapy.Spider):
    name = 'lianjiaSpider'
    allowed_domains = ['lianjia.com']

    # start_urls = ['https://sh.lianjia.com/zufang/pg'+str(i)+'/#contentList' for i in range(1,101)]
    start_urls=get_start_urls()
    def parse(self, response):
        item=LianjiaItem()
        selectors=response.xpath('''//*[@id="content"]/div[1]/div[1]/div''')
        # print(len(selectors))
        for selector in selectors:
            area=selector.xpath('''./div/p[2]/a[1]/text()''').get()
            adress = selector.xpath('''./div/p[2]/a[2]/text()''').get()
            img_url = selector.xpath('''./a/img/@src''').get()
            detail_url = 'https://sh.lianjia.com'+selector.xpath('''./div/p[1]/a/@href''').get()
            item['area']=area.strip()
            item['adress'] = adress.strip()
            item['img_url'] = img_url
            item['url']=detail_url
            # community = selector.xpath('''./div[1]/div/p[1]/a/text()''')
            yield Request(detail_url, callback=self.detail_parse,meta={'item':copy.deepcopy(item)})
            # request=Request(detail_url,callback=self.detail_parse)
            # request.meta['item']=item
            # return request
    def detail_parse(self,response):
        # print('*'*60)
        # print(response.url)
        item=response.meta['item']
        # print(item['url'])
        # print('*' * 60)
        community=response.xpath('''/html/body/div[4]/div[1]/div[3]/p/text()''').get()
        community = re.findall('·(.*?)\s', community)[0]
        shelf_time = response.xpath('''/html/body/div[4]/div[1]/div[3]/div[1]''').get()
        shelf_time=re.findall("房源上架时间 (.*?)\s",shelf_time,re.M)[0]
        id=response.xpath('''/html/body/div[4]/div[1]/div[3]/div[1]/i[2]/text()''').get()
        id = id.split('：')[-1]
        rent=response.xpath('''//*[@id="aside"]/p[1]/span/text()''').get().strip()
        type=response.xpath('''//*[@id="aside"]/ul[1]/p''')
        # rent_type=type.xpath('''./span[1]/text()''').get().strip()
        house_type = type.xpath('''./span[2]/text()''').get().strip()
        square = type.xpath('''./span[3]/text()''').get().strip()
        towards = type.xpath('''./span[4]/text()''').get().strip()
        floor=response.xpath('''/html/body/div[4]/div[1]/div[3]/div[2]/div[2]/ul/li[8]/text()''').get()
        floor = floor.split('：')[-1]
        #可能没有
        describe=response.xpath('''//*[@id="desc"]/ul/li/p[1]/text()''').get()
        subway=response.xpath('''string(//*[@id="around"]/ul)''').get()
        if subway:
            subway = subway.strip()
            subway=re.sub('\s+',' ',subway)
            # print(subway)
        download_time=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        item['id'] = id
        item['community']=community
        item['shelf_time'] = shelf_time
        item['rent'] = rent
        # item['rent_type'] = rent_type
        item['house_type'] = house_type
        item['square'] = square
        item['towards'] = towards
        item['floor'] = floor
        item['describe'] = describe
        item['subway'] = subway
        item['download_time'] = download_time
        yield item







