import sys
sys.path.append(".")
from urllib.parse import urlparse

from dao.redis_dao import r

QUEUE_PREFIX = "queue_"
SET_PREFIX = "set_"

def push(url):
    url_obj = urlparse(url)
    queue_key = QUEUE_PREFIX+url_obj.netloc
    if check(url):
        r.lpush(queue_key, url) 

def check(url):
    url_obj = urlparse(url)
    set_key = SET_PREFIX+url_obj.netloc
    return r.sadd(set_key, url) == 1


def poll(uuid):
    queue_key = QUEUE_PREFIX+uuid
    return r.lpop(queue_key)
    pass


if __name__ == '__main__':
    print(poll('www.baidu.com'))
