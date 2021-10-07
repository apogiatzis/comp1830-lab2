
import json
import requests

# Target address
address = '<address here>'

resp = requests.get('https://blockchain.info/unspent?active=%s' % address)
utxo_set = json.loads(resp.text)["unspent_outputs"]

for utxo in utxo_set:
    print("{tx_hash}:{tx_output_n} - {value} Satoshis".format(**utxo))
