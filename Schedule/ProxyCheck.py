import sys

sys.path.append('../')

from Proxy.ProxyManager import ProxyManager
from Util.UtilFunction import proxy_useful_valid
from Util.LogHandler import LogHandler
from threading import Thread
from time import sleep


class ProxyCheck(ProxyManager, Thread):
    """
    检查useful中的代理，不可用的删除
    """
    def __init__(self):
        ProxyManager.__init__(self)
        Thread.__init__(self)
        self.log = LogHandler('ProxyCheck')

    def run(self):
        self.log.info('Proxy useful check start')
        while True:
            self.db_client.change_table(self.useful_proxy)
            proxy = self.db_client.pop()
            while proxy:
                if proxy_useful_valid(proxy):
                    self.log.info('Proxy useful valid pass {}'.format(proxy))
                    self.db_client.put(proxy)
                else:
                    self.log.info('Proxy useful valid failed {}'.format(proxy))
                    self.db_client.delete(proxy)
                proxy = self.db_client.pop()
            self.log.info('Proxy useful check pausing')
            sleep(5 * 60)


if __name__ == '__main__':
    p = ProxyCheck()
    p.run()
