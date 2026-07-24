import requests
from config import API_KEY

def get_price(symbol):
    url = f"https://api.twelvedata.com/price?symbol={symbol}&apikey={API_KEY}"

    response = requests.get(url)
    data = response.json()

    if "price" in data:
        return data["price"]

    return None