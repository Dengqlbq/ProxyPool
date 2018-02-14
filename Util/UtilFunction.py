from Util.WebRequest import WebRequest
from lxml import etree


def get_html_tree(url):
    wr = WebRequest()
    html = wr.get(url).content
    return etree.HTML(html)
