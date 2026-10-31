import requests
import pandas as pd

API_KEY = 'YOU_API_KAY'
API_URL = "https://www.alphavantage.co/query"

parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": "TSLA",
    "apikey": API_KEY,
}

# Fazer pedido à API
response = requests.get(API_URL, params=parameters)
response.raise_for_status()

# Converter resposta JSON para dicionário Python
prices = response.json()


# OPTION 1 - Using Python dictionaries

daily_data = prices["Time Series (Daily)"]

dates = list(daily_data.keys())

latest_day = dates[0]
previous_day = dates[1]

latest_close = float(daily_data[latest_day]["4. close"])
previous_close = float(daily_data[previous_day]["4. close"])

#Calcular variação
def variation(latest_close, previous_close):
    return round((latest_close - previous_close) / previous_close * 100, 2)



# OPTION 2 - Using Pandas
"""
df = pd.DataFrame.from_dict(
    prices["Time Series (Daily)"],
    orient="index"
)

latest_close = float(df.iloc[0]["4. close"])
previous_close = float(df.iloc[1]["4. close"])
"""