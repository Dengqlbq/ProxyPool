import sys

sys.path.append('../')

from multiprocessing import Process
from Api.ProxyApi import run as ApiRun
from Schedule.ProxyValidSchedule import run as ValidRun
from Schedule.ProxyRefreshSchudule import run as RefreshRun


def run():
    pl = []
    p1 = Process(target=ApiRun, name='ApiRun')
    pl.append(p1)
    p2 = Process(target=RefreshRun, name='RefreshRun')
    pl.append(p2)
    p3 = Process(target=ValidRun, name='ValidRun')
    pl.append(p3)

    for p in pl:
        p.deamon = True
        p.start()
    for p in pl:
        p.join()


if __name__ == '__main__':
    run()

