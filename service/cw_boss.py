# -*- coding: UTF-8 -*-
import sys
sys.path.append(".")
from dao import movies_dao
from utils import crawler_utils as cu
from scheduler import redis_scheduler as scheduler

'''
boss直俜工作数据爬虫
http://www.zhipin.com/c101210100-p100101/y_4-b_%E4%BD%99%E6%9D%AD%E5%8C%BA/?ka=sel-industry-0
'''

links_ruls = {
    "find_page_rule": "//div[@class='page']/a/@href",
    "find_detail_rule": "//div[@class='info-primary']/h3[@class='name']/a/@href"
}

message_rules = {
    "company":"//div[@class='info-company']/h3[@class='name']/a/text()",#公司
    "post":"//div[@class='job-banner']/div/div/div[@class='info-primary']/div[@class='name']/text()",#职位
    # # "post_describe":"",#职位描述
    # # "request":"",#职位要求
    "salary":"//div[@class='job-banner']/div/div/div[@class='info-primary']/div[@class='name']/span/text()",#薪资
    "location":"//div[@class='job-location']/div[@class='location-address']/text()",#公司地址
    "work_time":"//div[@id='main']/div[@class='job-banner']/div/div/div[@class='info-primary']/p/text()[2]",#从业时间
    "education":"//div[@id='main']/div[@class='job-banner']/div/div/div[@class='info-primary']/p/text()[3]",#教育程度
    "financing":"//div[@class='info-company']/p[1]/text()[1]",#融资情况
    "company_size":"//div[@class='info-company']/p[1]/text()[2]",#公司规模
    "business":"//div[@id='main']/div[@class='job-banner']/div/div/div[@class='info-company']/p[1]/a/text()",#公司业务
    "web_site":"//div[@id='main']/div[@class='job-banner']/div/div/div[@class='info-company']/p[2]/text()"#公司官网
}

if __name__ == '__main__':
    url1 = 'http://www.zhipin.com/job_detail/1415200923.html?ka=search_list_1'
    url2 = 'http://www.zhipin.com/c101210100-p100101/y_4-b_%E4%BD%99%E6%9D%AD%E5%8C%BA/?ka=sel-industry-0'
    # html = cu.get_html_js(url1)
    # r = cu.analysis_detail_html(html ,message_rules)
    # r["resource_url"] = url1

    html = cu.get_html_js(url2)
    hostname = cu.getHostname(url2)
    print(hostname)
    r1 = cu.get_url(html, links_ruls['find_page_rule'],hostname)
    for link in r1:
        scheduler.push(link)
    r2 = cu.get_url(html, links_ruls['find_detail_rule'], hostname)
    for link in r2:
        scheduler.push(link)
    # print(r1)
    # print(r2)