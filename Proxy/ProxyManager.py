import sys

sys.path.append('../')

from Proxy.ProxyGetter import ProxyGetter
from Db.DbClient import DbClient
from Util.ConfigGetter import Config


class ProxyManager():
    """
    代理管理类
    """
    def __init__(self):
        self.db_client = DbClient()
        self.config = Config()

    def refresh(self):
        """
        获取新代理放入raw中
        :return:
        """
        proxies = set()
        for func in self.config.get_proxy_function:
            fc = getattr(ProxyGetter, func)
            for proxy in fc():
                proxies.add(proxy)

        for proxy in proxies:
            # useful集合中
            if self.db_client.exists(proxy):
                continue
            # raw集合中
            self.db_client.put(proxy)

    def get(self):
        """
        返回useful中一个代理
        :return:
        """
        return self.db_client.get()

    def get_all(self):
        """
        返回useful中所有代理
        :return:
        """
        return self.db_client.get_all()

    def get_status(self):
        """
        获取代理存储状态
        :return:
        """
        return self.db_client.get_status()


if __name__ == '__main__':
    m = ProxyManager()
    m.refresh()
    print(m.get_all())
    print(m.get_status())
