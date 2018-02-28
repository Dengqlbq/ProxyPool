import sys

sys.path.append('../')

from Proxy.ProxyManager import ProxyManager
from Util.UtilFunction import proxy_useful_valid
from Util.LogHandler import LogHandler
from threading import Thread
from apscheduler.schedulers.blocking import BlockingScheduler


class ProxyRefreshSchedule(ProxyManager):
    """
    定时刷新raw中代理，将可用代理放入useful
    """
    def __init__(self):
        ProxyManager.__init__(self)
        self.log = LogHandler('ProxyRefresh')

    def start(self):
        self.db_client.change_table(self.raw_proxy)
        proxy = self.db_client.pop()
        while proxy:
            if proxy_useful_valid(proxy):
                self.log.info('Proxy valid pass {}'.format(proxy))
                self.db_client.change_table(self.useful_proxy)
                self.db_client.put(proxy)
                self.db_client.change_table(self.raw_proxy)
            else:
                self.log.info('Proxy valid failed {}'.format(proxy))
            proxy = self.db_client.pop()


def refresh_pool():
    prs = ProxyRefreshSchedule()
    prs.start()


def mul_thread_refresh(threads=10):
    """
    多线程刷新代理
    :param threads:线程数量
    :return:
    """
    p = ProxyRefreshSchedule()
    # 获取新代理
    p.refresh()

    pl = []
    # 多线程检查
    for i in range(threads):
        p = Thread(target=refresh_pool, args=())
        pl.append(p)
    for p in pl:
        p.deamon = True
        p.start()
    for p in pl:
        p.join()


def run():
    """
    定时刷新
    :return:
    """
    mul_thread_refresh()
    schedule = BlockingScheduler()
    schedule.add_job(mul_thread_refresh, 'interval', minutes=1)
    schedule.start()


if __name__ == '__main__':
    run()
