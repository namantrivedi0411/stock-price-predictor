from flask import Flask, jsonify
from flask_cors import CORS
import yfinance as yf
import joblib

app = Flask(__name__)
CORS(app)

model = joblib.load("model.pkl")

@app.route("/predict/<ticker>")
def predict(ticker):

    data = yf.download(ticker, period="1y")

    close = data["Close"]

    prev_close = float(close.iloc[-1].iloc[0])
    ma50 = float(close.rolling(50).mean().iloc[-1].iloc[0])
    ma200 = float(close.rolling(200).mean().iloc[-1].iloc[0])
    
    print(type(prev_close))
    print(type(ma50))
    print(type(ma200))
    
    print(prev_close)
    print(ma50)
    print(ma200)

    pred = model.predict([[prev_close, ma50, ma200]])

    return jsonify({
        "ticker": ticker,
        "predicted_price": float(pred[0])
    })

if __name__ == "__main__":
    app.run(debug=True)