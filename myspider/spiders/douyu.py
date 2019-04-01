# -*- coding: utf-8 -*-
import scrapy, json
import time
from myspider.items import DyItem


class DouyuSpider(scrapy.Spider):
    name = 'douyu'
    allowed_domains = ['douyu.com']
    start_url = 'https://m.douyu.com/api/room/list?page=%s&type='
    start_page_num = 1239
    start_urls = [start_url % start_page_num]

    def parse(self, response):
        print('current request page num is %s' % DouyuSpider.start_page_num)
        #yield BaseItem, Request, dict, None
        res_data = json.loads(response.text).get('data')
        live_data = res_data.get('list')
        if not live_data:
            print('douyu response data is null!')
            return
        total_page = res_data.get('pageCount')
        dy = DyItem()
        for item in live_data:
            dy['nickname'] = item.get('nickname')
            dy['hn'] = item.get('hn')
            dy['roomName'] = item.get('roomName')
            dy['roomSrc'] = item.get('roomSrc')
            yield item
        time.sleep(3)
        DouyuSpider.start_page_num += 1
        if total_page < DouyuSpider.start_page_num:
            print('数据已全部解析完成!')
            return
        yield scrapy.Request(url=DouyuSpider.start_url % DouyuSpider.start_page_num)
        print('len live item one page is ', len(live_data))
