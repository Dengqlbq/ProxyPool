import sys

sys.path.append('../')

import redis


class RedisClient():

    def __init__(self, host, port):
        self._conn = redis.Redis(host, port)

    def get(self):
        """
        从数据库的useful中返回一个代理
        :return:
        """
        proxy = self._conn.srandmember('useful')
        if proxy:
            return proxy.decode('ascii')
        return None

    # 存放方式待改进
    def put(self, proxy, sname='raw'):
        """
        将proxy放入数据库的sname表中
        :param proxy:
        :param sname:表名
        :return:
        """
        return self._conn.sadd(sname, proxy)

    def get_all(self):
        """
        从数据库的useful中返回所有代理
        :return:
        """
        proxies = self._conn.smembers('useful')
        if proxies:
            proxy_list = []
            for i in proxies:
                proxy_list.append(i.decode('ascii'))
            return proxy_list
        return None

    def get_status(self):
        """
        返回数据库中代理的存储状态
        :return:
        """
        status = dict()
        status['useful'] = self._conn.scard('useful')
        status['raw'] = self._conn.scard('raw')
        return status

    def exists(self, proxy):
        """
        判断proxy是否存在数据库的useful中
        :param proxy:
        :return:
        """
        return self._conn.sismember('useful', proxy)

    def pop(self, sname):
        """
        从数据库的sname表中弹出一个代理
        :param sname:表名
        :return:
        """
        proxy = self._conn.spop(sname)
        if proxy:
            return proxy.decode('ascii')
        else:
            return None

    def delete(self, proxy, sname):
        """
        从sname表中删除指定代理
        :param proxy:
        :param sname: 表名
        :return:
        """
        self._conn.srem(sname, proxy)


if __name__ == '__main__':

    r = redis.Redis('zzzzz', '6379')
    print(r.spop('raw'))
    print(r.spop('raw'))

