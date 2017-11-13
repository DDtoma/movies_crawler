import redis

import config

config = config.config
pool = redis.ConnectionPool(host=config.redis_host, port=config.redis_port, password=config.redis_pasword)
r = redis.StrictRedis(connection_pool = pool)
