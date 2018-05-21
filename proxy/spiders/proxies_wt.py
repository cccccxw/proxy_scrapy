# -*- coding: utf-8 -*-
import scrapy
from proxy.items import ProxyItem

class ProxiesSpider(scrapy.Spider):
    name = 'proxies_wt'
    allowed_domains = ['www.xicidaili.com/wt']
    start_urls = ['http://www.xicidaili.com/wt/']
    global count
    count = 1 


    def parse(self, response):
        global count
        count = count - 1
        proxies = response.css('table tr')
        for proxie in proxies:
            item = ProxyItem()
            ip = proxie.css('td:nth-child(2)::text').extract_first()
            port = proxie.css('td:nth-child(3)::text').extract_first()
            speed = proxie.css('td:nth-child(7) div::attr(title)').extract_first()
            item['ip'] = ip
            item['port'] = port
            item['speed'] = speed
            yield item
        if count:
            next = response.css('.pagination .next_page::attr(href)').extract_first()
            page = response.css('.pagination .current::text').extract_first()
            url = response.urljoin(next)
            yield scrapy.Request(url = url, callback= self.parse,dont_filter=True)