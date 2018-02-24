import sys

sys.path.append('../')

from Schedule.ProxyCheck import ProxyCheck


class ProxyValidSchedule():

    def __init__(self):
        pass

    def start(self, threads=5):
        pl = []
        for i in range(threads):
            pl.append(ProxyCheck())
        for i in pl:
            i.deamon = True
            i.start()
        for i in pl:
            i.join()


def run():
    pp = ProxyValidSchedule()
    pp.start()


if __name__ == '__main__':
    p = ProxyValidSchedule()
    p.start()

