from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from contractabi import abi,bytecode
import logging

import os
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:password@localhost:5432/ARTHA'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
migrate = Migrate(app, db)
from web3 import Web3
contractaddress=Web3.toChecksumAddress('0xac791d7a14473C1309Ee588F49c9FA9293055Df3')

w3 = Web3(Web3.HTTPProvider('http://127.0.0.1:7545'))
w3.eth.default_account = w3.eth.accounts[0]
testcall = w3.eth.contract(
   address=contractaddress,
    abi=abi
 )

from models import Coin

@app.route("/")
def home():
    return "Hello, Flask!"


@app.route("/coindata", methods = ['POST','GET'])
def coindata():
    if request.method=='POST':
        coinaddress= request.form['coinid']
        price=request.form['price']
        indicator1=request.form['indicator1']
        indicator2=request.form['indicator2']
        app.logger.info(coinaddress+price,indicator1,indicator2)
        coin=Coin(
        price=price,
        indicator1=indicator1,
        indicator2=indicator2
        )
        db.session.add(coin)
        db.session.commit()
        tx_hash = testcall.functions.addData(coin.id,price,int(coin.timestamp),indicator1,indicator2).transact()
        return jsonify(coin.serialize())

    elif request.method=='GET':
        coinid= request.args.get('coinid')
        logconsole = logging.getLogger(coinid)
        result= testcall.functions.collectedDatabyTid(int(coinid)).call()
        return str(result)