import sys

sys.path.append('../')

import redis


class RedisClient():

    def __init__(self, host, port):
        self._conn = redis.Redis(host, port)

    def get(self):
        proxy = self._conn.srandmember('useful')
        if proxy:
            return proxy.decode('ascii')
        return None

    # 存放方式待改进
    def put(self, proxy, sname='useful'):
        return self._conn.sadd(sname, proxy)

    def get_all(self):
        proxies = self._conn.smembers('useful')
        if proxies:
            proxy_list = []
            for i in proxies:
                proxy_list.append(i.decode('ascii'))
            return proxy_list
        return None

    def get_status(self):
        status = dict()
        status['useful'] = self._conn.scard('useful')
        status['raw'] = self._conn.scard('raw')
        return status


if __name__ == '__main__':
    r = RedisClient('120.79.155.23', '6379')
    print(r.get())
    print(r.get_all())

