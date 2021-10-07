from web3 import Web3

rpc_node='https://speedy-nodes-nyc.moralis.io/46fb5bf54b9f7ee7eb4b0a54/eth/mainnet' 
w3 = Web3(Web3.HTTPProvider(rpc_node))

account = "<address here>"

def get_balance(address):
    return w3.eth.getBalance(w3.toChecksumAddress(address))

print(f"Balance for {account}:")
print(get_balance(account))