import sys

sys.path.append('../')

from flask import Flask, jsonify
from Util.ConfigGetter import Config
from Db.DbClient import DbClient

c = Config()
db = DbClient()

app = Flask('ProxyPool')


@app.route("/")
def hello():
    return 'Hello Coder'


@app.route("/get")
def get():
    return jsonify(db.get())


@app.route("/get_all")
def get_all():
    return jsonify(db.get_all())


@app.route("/get_status")
def get_status():
    return jsonify(db.get_status())


if __name__ == '__main__':
    app.run()



