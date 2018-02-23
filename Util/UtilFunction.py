from Util.WebRequest import WebRequest
from lxml import etree
import re
import requests


def get_html_tree(url):
    """
    获取html树
    :param url:
    :return:
    """
    wr = WebRequest()
    html = wr.get(url).content
    return etree.HTML(html)


def proxy_format_valid(proxy):
    """
    检验代理格式是否正确
    :param proxy:
    :return:
    """
    ls = re.findall(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}:\d{1, 5}', proxy)
    return True if len(ls) == 1 and ls[0] == proxy else False


def proxy_useful_valid(proxy):
    """
    检验代理是否可用
    :param proxy:
    :return:
    """
    proxies = {"http": "http://{0}".format(proxy)}
    try:
        r = requests.get('http://httpbin.org/ip', proxies=proxies, timeout=10, verify=False)
        if r.status_code == 200:
            return True
    except Exception as e:
        return False


if __name__ == '__main__':
    proxy_useful_valid('183.52.197.65:1087')
