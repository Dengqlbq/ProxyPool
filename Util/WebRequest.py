import requests


class WebRequest():

    def __init__(self):
        pass

    @property
    def header(self):
        headers = {
           'Accept-Encoding': 'gzip, deflate',
           'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
           'Connection': 'keep-alive',
           'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8',
           'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) '\
                         'Chrome/62.0.3202.94 Safari/537.36'
        }
        return headers

    # 很多处理没做
    def get(self, url, header=None):
        headers = self.header
        if header and isinstance(header, dict):
            headers.update(header)
        html = requests.get(url, headers=headers)
        return html


if __name__ == '__main__':
    w = WebRequest()
    print(w.get('http://www.xdaili.cn/freeproxy').text)
