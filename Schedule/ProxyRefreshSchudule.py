import sys

sys.path.append('../')

from Proxy.ProxyManager import ProxyManager
from Util.UtilFunction import proxy_useful_valid
from threading import Thread
from apscheduler.schedulers.blocking import BlockingScheduler


class ProxyRefreshSchedule(ProxyManager):
    """
    定时刷新raw中代理，将可用代理放入useful
    """

    def __init__(self):
        ProxyManager.__init__(self)
        self.raw_set = 'raw'
        self.useful_set = 'useful'

    def start(self):
        proxy = self.db_client.pop(self.raw_set)
        while proxy:
            if proxy_useful_valid(proxy):
                self.db_client.put(proxy, self.useful_set)
                print('proxy valid {}'.format(proxy))
            else:
                print('proxy not valid {}'.format(proxy))
            proxy = self.db_client.pop(self.raw_set)


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
    schedule.add_job(mul_thread_refresh, 'interval', minutes=5)
    schedule.start()


if __name__ == '__main__':
    run()
