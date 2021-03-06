from flask import Flask, request
from utills import currency_calc

app = Flask(__name__)


@app.route("/btc-rate")
def get_bitcoin_rate():

    cur = request.args.get('currency', 'USD')
    return currency_calc(cur)


app.run(debug=True)
