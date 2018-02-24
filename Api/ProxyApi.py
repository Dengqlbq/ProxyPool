import sys

sys.path.append('../')

from flask import Flask, jsonify
from Proxy.ProxyManager import ProxyManager


app = Flask('ProxyPool')


@app.route("/")
def hello():
    return 'Hello Coder'


# 返回单个proxy带有双引号，待解决
@app.route("/get")
def get():
    return jsonify(ProxyManager().get())


@app.route("/get_all")
def get_all():
    return jsonify(ProxyManager().get_all())


@app.route("/get_status")
def get_status():
    return jsonify(ProxyManager().get_status())


def run():
    app.run()


if __name__ == '__main__':
    app.run()



