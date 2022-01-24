from flask import Flask, jsonify, request
import os
import yaml

app = Flask(__name__)
app.config["JSON_AS_ASCII"] = False  # jsonify返回的中文正常显示

def read_yaml(path):
    with open(path, 'rb') as f:
        cf= f.read()
    cf = yaml.load(cf)
    return cf

@app.route('/')
def hello_world():
    return 'Hello World! I am mock!'


@app.route('/test')
def test():
    r = read_yaml(os.getcwd()+'/data/test.txt')
    return jsonify({"code": 1001, "msg": r})

#发票申请接口
@app.route('/fapiaoApply')
def fapiaoApply():
    r = read_yaml(os.getcwd()+'/data/test.txt')
    return jsonify({"code": 2001, "msg": r})

#发票查询接口
@app.route('/fapiaoCheck')
def fapiaoCheck():
    r = read_yaml(os.getcwd()+'/data/test.txt')
    return jsonify({"code": 3001, "msg": r})

