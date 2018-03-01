import redis


class RedisClient():

    def __init__(self, table, host, port):
        self._table = table
        self._conn = redis.Redis(host=host, port=port, db=0)

    def get(self):
        """
        从数据库的中返回一个代理
        :return:
        """
        proxy = self._conn.srandmember(self._table)
        if proxy:
            return proxy.decode('ascii')
        return None

    def put(self, proxy):
        """
        将proxy放入数据库
        :param proxy:
        :return:
        """
        return self._conn.sadd(self._table, proxy)

    def get_all(self):
        """
        从数据库中返回所有代理
        :return:
        """
        proxies = self._conn.smembers(self._table)
        if proxies:
            proxy_list = []
            for i in proxies:
                proxy_list.append(i.decode('ascii'))
            return proxy_list
        return None

    def get_status(self):
        """
        返回数据库中指定表代理的存储状态
        :return:
        """
        return self._conn.scard(self._table)

    def exists(self, proxy):
        """
        判断proxy是否存在数据库中
        :param proxy:
        :return:
        """
        return self._conn.sismember(self._table, proxy)

    def pop(self):
        """
        从数据库中弹出一个proxy
        :return:
        """
        proxy = self._conn.spop(self._table)
        if proxy:
            return proxy.decode('ascii')
        else:
            return None

    def delete(self, proxy):
        """
        从数据中删除一个代理
        :param proxy:
        :return:
        """
        self._conn.srem(self._table, proxy)

    def change_table(self, table):
        """
        改变当前数据库表
        :param table:
        :return:
        """
        self._table = table
