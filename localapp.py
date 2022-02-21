from web3 import Web3

ganache_url = "http://127.0.0.1:7545"
web3 = Web3(Web3.HTTPProvider(ganache_url))

print(web3.isConnected())
# print(web3.eth.blockNumber)

account_1 = "0x929545A033AC4F97E57b0a7F894C28543C5Ec86A"
account_2 = "0x7f477E01D8376c2819B6257daE4b049D874D4BA2"

private_key = "0x8ed9aefd03409b649842e58670ffd063fc1a5cb62737d52ae76cbfe3b825139c"

balance = web3.eth.getBalance("0x7f477E01D8376c2819B6257daE4b049D874D4BA2")

print(balance)

nonce = web3.eth.getTransactionCount(account_1)

tx = {
    'nonce': nonce,
    'to': account_2,
    'value': web3.toWei(1,'ether'),
    'gas': 2000000,
    'gasPrice': web3.toWei('50', 'gwei')
}

signed_tx = web3.eth.account.signTransaction(tx, private_key)
tx_hash = web3.eth.sendRawTransaction(signed_tx.rawTransaction)

print(web3.toHex(tx_hash), web3.eth.blockNumber)