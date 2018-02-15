from configparser import ConfigParser
import os


class Config():

    def __init__(self):
        self.current_path = os.path.split(os.path.abspath(__file__))[0]
        self.file_path = os.path.join(os.path.split(self.current_path)[0], 'Config.ini')
        self.parser = ConfigParser()
        self.parser.read(self.file_path)

    # 所有返回数据都是字符串，配置中无需手动添加引号
    @property
    def db_host(self):
        return self.parser['Database']['Host']

    @property
    def db_port(self):
        return self.parser['Database']['Port']

    @property
    def db_type(self):
        return self.parser['Database']['Type']

    @property
    def get_proxy_function(self):
        for func in self.parser['GetProxyFunction']:
            if self.parser['GetProxyFunction'][func] == '1':
                yield func


if __name__ == '__main__':
    c = Config()
    print(c.db_host)
    print(c.db_port)
    for i in c.get_proxy_function:
        print(i)
