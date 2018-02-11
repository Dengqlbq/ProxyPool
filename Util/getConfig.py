from configparser import ConfigParser
import os


class Config():

    def __init__(self):
        self.current_path = os.path.split(os.path.abspath(__file__))[0]
        self.file_path = os.path.join(os.path.split(self.current_path)[0], 'Config.ini')
        self.parser = ConfigParser()
        self.parser.read(self.file_path)

    @property
    def db_host(self):
        return self.parser['Database']['Host']

    @property
    def db_port(self):
        return self.parser['Database']['Port']


if __name__ == '__main__':
    c = Config()
    print(c.db_host)
    print(c.db_port)
