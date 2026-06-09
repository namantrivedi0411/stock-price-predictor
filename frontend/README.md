# Stock Price Predictor

A machine learning-based stock price prediction system built using Python, Scikit-Learn, Flask, and Yahoo Finance.

## Features

- Download real stock data using Yahoo Finance
- Data visualization with Matplotlib and Seaborn
- Multiple ML models:
  - Linear Regression
  - Lasso Regression
  - Ridge Regression
  - Support Vector Regression (SVR)
- REST API using Flask
- Predict stock prices using historical trends

## Tech Stack

- Python
- Flask
- Scikit-Learn
- Pandas
- NumPy
- Yahoo Finance API

## Run Locally

```bash
pip install -r requirements.txt
python app.py
```

API:

```bash
http://127.0.0.1:5000/predict/AAPL
```