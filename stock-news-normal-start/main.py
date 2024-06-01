import requests 
import os


import sys
sys.path.append(r'c:\users\sansk\appdata\local\programs\python\python38\lib\site-packages')


from twilio.rest import Client

account_sid = 'AC2be3cd3b78ee8d11c4e479cbf9db6320'
auth_token = 'f42ffd457f82f621600f3663e77debbf'
client = Client(account_sid, auth_token)

# Stock and news API credentials
STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"
newsapi = "510a0c4e8f0f483b865551673c4fe98e"
alphavantage = "T8N0Z5DDMXO4ZNCF"

# API endpoints
STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

# Get stock data
stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": alphavantage,
}

response = requests.get(STOCK_ENDPOINT, params=stock_params)
data = response.json()["Time Series (Daily)"]

data_list = [value for (key, value) in data.items()]

yesterday_data = data_list[0]
yesterday_closing_price = float(yesterday_data["4. close"])

day_before_yesterday_data = data_list[1]
day_before_yesterday_closing_price = float(day_before_yesterday_data["4. close"])


difference = yesterday_closing_price - day_before_yesterday_closing_price
up_down = "🔺👆" if difference > 0 else "🔻👇"
diff_percent = round(abs(difference) / day_before_yesterday_closing_price * 100, 2)

if diff_percent > 2:
    news_params = {
        "apiKey": newsapi,
        "qInTitle": COMPANY_NAME,
    }

    news_response = requests.get(NEWS_ENDPOINT, params=news_params)
    articles = news_response.json()["articles"][:3]

    
    formatted_articles = [
        f"{STOCK_NAME}: {up_down} {diff_percent}%\nHeadline: {article['title']}\nDescription: {article['description']}"
        for article in articles
    ]
    print(formatted_articles)
  
    for article in formatted_articles:
        message = client.messages.create(
            body=article,
            from_='+12232707281',  
            to='+917983438874'
        )
        print(f"Message sent: {message.sid}")