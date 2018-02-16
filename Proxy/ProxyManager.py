import sys

sys.path.append('../')

from Proxy.ProxyGetter import ProxyGetter
from Db.DbClient import DbClient
from Util.ConfigGetter import Config


class ProxyManager():

    def __init__(self):
        self.db_client = DbClient()
        self.config = Config()

    def refresh(self):
        for func in self.config.get_proxy_function:
            fc = getattr(ProxyGetter, func)
            for proxy in fc():
                self.db_client.put(proxy, sname='raw')

    def get(self):
        return self.db_client.get()

    def get_all(self):
        return self.db_client.get_all()

    def get_status(self):
        return self.db_client.get_status()


if __name__ == '__main__':
    m = ProxyManager()
    m.refresh()
    print(m.get_all())
    print(m.get_status())
