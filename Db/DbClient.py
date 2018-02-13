import sys
import os
from Util.getConfig import Config

sys.path.append(os.path.dirname(__file__))


# 数据库工厂类
class DbClient():

    def __init__(self):
        self.config = Config()
        self.init_db_client()

    def init_db_client(self):
        # 所有支持的数据库类型
        types = ['Redis']
        db_type = self.config.db_type
        assert db_type in types, 'DbTypeError: not support {}'.format(db_type)
        self.client = getattr(__import__(db_type + 'Client'), db_type + 'Client')(self.config.db_host,
                                                                                  self.config.db_port)

    def get(self):
        return self.client.get()

    def put(self, *args, **kwargs):
        self.client.put(*args, **kwargs)

    def get_all(self):
        return self.client.get_all()

    def get_status(self):
        return self.client.get_status()


if __name__ == '__main__':
    db = DbClient()
    db.put('se2')
    db.put('aaa2', sname='raw')
    print(db.get())
    print(db.get_all())
    print(db.get_status())
