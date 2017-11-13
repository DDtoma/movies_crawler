# -*- coding: UTF-8 -*-
from dao import movies_dao
from utils import crawler_utils as cu
import re
'''
bt电影天堂爬虫
http://www.btbtdy.com/btfl/dy1.html
'''

hostname = 'http://www.btbtdy.com'

message_rules = {
    'name': "//div[@class='vod_intro rt']/h1/text()",
    'link_name': "//div[@class='p_list']/ul/li/a/@title",
    'bt_link': "//div[@class='p_list']/ul/li/span/a/@href"
}

links_ruls = {
    "find_page_rule": "//div[@class='pages']/a/@href",
    "find_detail_rule": "//div[@class='liimg']/a/@href"
}

page_links = set([])
detail_links = set([])

def start(start_url):
    '''
    爬虫的主控
    :param start_url:
    :return:
    '''
    global page_links
    global detail_links

    html = cu.get_html(start_url)
    hostname = cu.getHostname(start_url)
    plinks_list = cu.get_url(html, links_ruls["find_page_rule"], hostname)
    last_page_link = plinks_list[-1]
    result = re.findall(r'\d+', last_page_link)[1]

    for i in range(int(result)):
        page_links.add('http://www.btbtdy.com/btfl/dy1-'+str(i)+'.html')

    while(page_links.__len__() != 0):
        link = page_links.pop()
        html = cu.get_html(link)
        dl = cu.get_url(html, links_ruls['find_detail_rule'], hostname)

        if isinstance(dl, list):
            detail_links = detail_links.union(set(dl))

        if isinstance(dl, set):
            detail_links = detail_links.union(dl)

        if isinstance(dl, str):
            detail_links.add(dl)

    while(detail_links.__len__() != 0):
        link = detail_links.pop()
        html = cu.get_html_js(link)
        if html is not None:
            movie_massage = cu.analysis_detail_html(html, message_rules)
            movie_massage['source_link']=link
            movie_massage['host']=hostname
            print(movie_massage)
            movies_dao.insert_moveis(movie_massage)

if __name__ == '__main__':
    start("http://www.btbtdy.com/btfl/dy1.html")
