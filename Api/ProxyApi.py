import sys

sys.path.append('../')

from flask import Flask, jsonify
from Proxy.ProxyManager import ProxyManager
from Util.ConfigGetter import Config


app = Flask('ProxyPool')


@app.route("/")
def hello():
    return 'Hello Coder'


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
    app.run(host=Config().proxy_pool_host, port=Config().proxy_pool_port)


if __name__ == '__main__':
    app.run()



