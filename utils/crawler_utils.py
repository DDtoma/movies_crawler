# -*- coding: UTF-8 -*-
from lxml import etree
from selenium import webdriver
import requests

headers = {"headers": "User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Safari/604.1.38"}

def get_url(html, find_url_rule, hostname=''):
    '''
    解析页面活动链接
    :param html:
    :param find_url_rule:
    :return:
    '''
    page_links_list = []
    selector = etree.HTML(html)
    if find_url_rule is not None:
        p_links_tmp = selector.xpath(find_url_rule)
        for link in p_links_tmp:
            # page_links_list.add(hostname + str(link))
            page_links_list.append(hostname + str(link))
    return page_links_list

def analysis_detail_html(html, rules):
    '''
    分析页面获得数据
    :param html: 网页源码
    :param rules: 匹配规则
    :return:
    '''
    result = {}
    selector = etree.HTML(html)
    for k in rules:
        rs = selector.xpath(rules[k])
        result[k]=rs
    return result

def get_html_js(url):
    '''
    请求网络获得页面（运行js）
    :param url:
    :return:
    '''
    try:
        service_args = []
        service_args.append('--load-images=no')  ##关闭图片加载
        service_args.append('--disk-cache=yes')  ##开启缓存
        service_args.append('--ignore-ssl-errors=true')  ##忽略https错误
        driver = webdriver.PhantomJS(service_args=service_args)
        driver.implicitly_wait(10)
        driver.set_page_load_timeout(10)
        driver.get(url)
        return driver.page_source.encode('utf-8')
    except Exception:
        return None


def get_html(url):
    '''
    请求网络获得页面
    :param url:
    :return:
    '''
    r= requests.get(url,headers=headers)
    if r.status_code == 200:
        return r.text.encode('utf-8')
    else:
        return None