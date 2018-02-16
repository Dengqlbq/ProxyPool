from Util.WebRequest import WebRequest
from lxml import etree
import re


def get_html_tree(url):
    wr = WebRequest()
    html = wr.get(url).content
    return etree.HTML(html)


def proxy_format_valid(proxy):
    ls = re.findall(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}:\d{1, 5}', proxy)
    return True if len(ls) == 1 and ls[0] == proxy else False
