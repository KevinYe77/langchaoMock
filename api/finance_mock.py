from flask import Flask, jsonify, request
import os
import yaml

app = Flask(__name__)
app.config["JSON_AS_ASCII"] = False  # jsonify返回的中文正常显示

def read_yaml(path):
    with open(path, 'rb') as f:
        cf= f.read()
    cf = yaml.safe_load(cf)
    return cf

@app.route('/')
def hello_world():
    return 'Hello World! I am mock!'



#收款认领接口
@app.route('/QueryReceipts')
def QueryReceipts():

    companyCode = request.args.get("CompanyCode")

    r = read_yaml(os.getcwd()+'/data/QueryReceipts.txt')
    list2= []
    for rs in r:
       if rs['CompanyCode'] == companyCode:
           list2.append(rs)

    return jsonify({"Count": len(list2), "Records": list2})


#收款认领反馈接口
@app.route('/ComfirmReceipts')
def ComfirmReceipts():
    SerialNo = request.args.get("SerialNo")
    Flag = request.args.get("Flag")

    r = read_yaml(os.getcwd()+'/data/ComfirmReceipts.txt')
    for rs in r:
       if rs['SerialNo'] == SerialNo and rs['Flag'] == Flag:
           hit = rs

    return jsonify({"Code": hit['Code'], "Message": hit['Message']})