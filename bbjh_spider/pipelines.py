# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from openpyxl import Workbook
import time

class BbjhSpiderPipeline(object):

    wb = Workbook()
    ws = wb.active
    ws.append(['url'])
    curtime = time.strftime("%Y%m%d", time.localtime())

    def process_item(self, item, spider):
        line = [item['url']]
        name = item['name']
        self.ws.append(line)
        self.wb.save('%s_%s.xlsx' % (name, self.curtime))
        return item
