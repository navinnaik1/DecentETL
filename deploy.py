
from contractabi import abi,bytecode
from web3 import Web3

w3 = Web3(Web3.HTTPProvider('http://127.0.0.1:7545'))
w3.eth.default_account = w3.eth.accounts[0]
test = w3.eth.contract(abi=abi, bytecode=bytecode)
tx_hash = test.constructor().transact()
tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
