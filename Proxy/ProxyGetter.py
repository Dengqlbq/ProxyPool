import sys

sys.path.append('../')

from Util.UtilFunction import get_html_tree


class ProxyGetter():

    def __init__(self):
        pass

    @staticmethod
    def get_proxy_one():
        url = 'http://www.data5u.com/free/index.shtml'
        html_tree = get_html_tree(url)
        proxies = html_tree.xpath('//ul[@class="l2"]')

        for proxy in proxies:
            ip = proxy.xpath('.//span[1]/li/text()')[0]
            port = proxy.xpath('.//span[2]/li/text()')[0]
            yield ip + ':' + port


if __name__ == '__main__':
    for i in ProxyGetter.get_proxy_one():
        print(i)
