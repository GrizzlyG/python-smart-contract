import json
from web3 import Web3

ganache_url = "http://127.0.0.1:7545"
web3 = Web3(Web3.HTTPProvider(ganache_url))

web3.eth.defaultAccouont = web3.eth.accounts[0]

print(web3.eth.defaultAccount)

j = '[{"inputs":[],"name":"greet","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"greeter","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"greeting","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"string","name":"_greeting","type":"string"}],"name":"setGreeting","outputs":[],"stateMutability":"nonpayable","type":"function"}]'
abi = json.loads(j)
address = web3.toChecksumAddress("0x20C9240AAEc8C3e6b78466DFf4b57bf4432a3Fb7")

contract = web3.eth.contract(address=address, abi=abi)

print("weitin")
tx_hash = contract.functions.setGreeting("taekwon").transact({'from': web3.eth.accounts[0], 'gasPrice': web3.eth.gasPrice, 'gas': web3.eth.getBlock('latest').gasLimit})

print("waiting")
web3.eth.waitForTransactionReceipt(tx_hash)

print("weiting")
print('Updated greeting:, {}'.format(
     contract.functions.greet().call()
))