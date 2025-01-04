import sys
# sys.path.append('C:/Users/mdhsn/OneDrive/Desktop/Bitcoin')
sys.path.append('c:/Users/Has/Desktop/Academic/Project/Bitcoin')

from flask import Flask, render_template, request
from Blockchain.client.sendBTC import sendBTC
from Blockchain.Backend.core.Tx import Tx

app = Flask(__name__)
@app.route('/', methods = ["GET", "POST"])
def wallet():
    message = ''

    if request.method == "POST":
        FromAddress = request.form.get("fromAddress")
        ToAddress = request.form.get("toAddress")
        Amount = request.form.get("Amount", type=int)
        sendCoin = sendBTC(FromAddress, ToAddress, Amount, UTXOS)
        TxObj =  sendCoin.prepareTransaction()
        scriptPubKey = sendCoin.scriptPubKey(FromAddress)
        varified = True

        if not TxObj:
            message = "Invalid Transaction"

        if isinstance(TxObj, Tx):
            for index, tx in enumerate(TxObj.tx_ins):
                if TxObj.verify_input(index, scriptPubKey):
                    varified = False
                
            if varified:
                MEMPOOL[TxObj.TxId] = TxObj
                message = "Transaction is added in the memory pool"


    return render_template('wallet.html', message = message)

def main(utxos, MemPool):
    global UTXOS
    global MEMPOOL
    
    UTXOS = utxos
    MEMPOOL = MemPool

    app.run()