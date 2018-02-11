import sys

sys.path.append('../')

from flask import Flask
from Util.getConfig import Config

c = Config()

app = Flask('ProxyPool')


@app.route("/")
def hello():
    return 'Hello Coder'


if __name__ == '__main__':
    app.run()



