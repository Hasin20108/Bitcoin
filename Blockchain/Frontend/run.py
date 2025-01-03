import sys
# sys.path.append('C:/Users/mdhsn/OneDrive/Desktop/Bitcoin')
sys.path.append('c:/Users/Has/Desktop/Academic/Project/Bitcoin')

from flask import Flask, render_template, request

from Blockchain.client.sendBTC import sendBTC

app = Flask(__name__)
@app.route('/', methods = ["GET", "POST"])
def wallet():
    message = ''

    if request.method == "POST":
        FromAddress = request.form.get("fromAddress")
        ToAddress = request.form.get("toAddress")
        Amount = request.form.get("Amount", type=int)
        sendCoin = sendBTC(FromAddress, ToAddress, Amount, UTXOS)

        if sendCoin.prepareTransaction():
            message = "Insufficient Balance"
    return render_template('wallet.html', message = message)

def main(utxos):
    global UTXOS
    UTXOS = utxos
    app.run()