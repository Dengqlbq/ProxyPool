import sys

sys.path.append('../')

from Util.UtilFunction import get_html_tree
from Util.WebRequest import WebRequest


class ProxyGetter():
    """
    代理获取类
    """
    def __init__(self):
        pass

    @staticmethod
    def get_proxy_one():
        """
        采集：http://www.ip181.com/
        :return:
        """
        url = 'http://www.ip181.com/'
        html = get_html_tree(url)
        nodies = html.xpath('//tr')[1:]
        for node in nodies:
            ip_port = node.xpath('.//td/text()')[0:2]
            yield ':'.join(ip_port)

    @staticmethod
    def get_proxy_two():
        """
        采集：http://www.xdaili.cn/freeproxy
        :return:
        """
        url = 'http://www.xdaili.cn/ipagent/freeip/getFreeIps?page=1&rows=10'
        request = WebRequest()
        res = request.get(url).json()
        for row in res['RESULT']['rows']:
            yield '{}:{}'.format(row['ip'], row['port'])

    @staticmethod
    def get_proxy_three():
        """
        采集：https://www.kuaidaili.com
        :return:
        """
        url = 'https://www.kuaidaili.com/free/inha/{}/'
        for i in range(1, 5):
            html = get_html_tree(url.format(i))
            nodies = html.xpath('//tr')
            for node in nodies:
                ip_port = node.xpath('.//td/text()')[0:2]
                yield ':'.join(ip_port)

    @staticmethod
    def get_proxy_forth():
        url = 'http://www.mogumiao.com/proxy/free/listFreeIp'
        request = WebRequest()
        res = request.get(url).json()
        for row in res['msg']:
            yield '{}:{}'.format(row['ip'], row['port'])


if __name__ == '__main__':
    for i in ProxyGetter.get_proxy_fifth():
        print(i)
