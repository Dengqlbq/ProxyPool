import sys

sys.path.append('../')

from Proxy.ProxyManager import ProxyManager
from Util.UtilFunction import proxy_useful_valid
from threading import Thread
from time import sleep


class ProxyCheck(ProxyManager, Thread):
    """
    检查useful中的代理，不可用的删除
    """
    def __init__(self):
        ProxyManager.__init__(self)
        Thread.__init__(self)

    def run(self):
        self.db_client.change_table(self.useful_proxy)
        while True:
            proxy = self.db_client.pop()
            while proxy:
                if proxy_useful_valid(proxy):
                    print('useful valid pass {0}'.format(proxy))
                    self.db_client.put(proxy)
                else:
                    print('useful valid faild {0}'.format(proxy))
                    self.db_client.delete(proxy)
                proxy = self.db_client.pop()
            sleep(1 * 60)


if __name__ == '__main__':
    p = ProxyCheck()
    p.run()
