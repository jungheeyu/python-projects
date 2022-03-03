import requests
from twilio.rest import Client

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
NUM_DAYS = 7

# API keys
ALPHA_VANTAGE_API_KEY = "VZRH7X9ZESYF9PFN"
NEWS_API_KEY = "3dc2973b61764b798f5169c2a94db50e"

# Set up for using Twilio
account_sid = 'ACedb1e46cd112da2013a9e0545d599efc'
auth_token = '800e75da517127180a0da3ddb39b35a8'
client = Client(account_sid, auth_token)

# Set up parameters for Alpha Vantage requests
url_alpha_vantage = 'https://www.alphavantage.co/query'
params_alpha_vantage = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": ALPHA_VANTAGE_API_KEY
}

# Set up parameters for News requests
url_news = "https://newsapi.org/v2/everything"
params_news = {
    "q": STOCK,
    "sortBy": "popularity",
    "apiKey": NEWS_API_KEY
}

# Get response for Alpha Vantage API
response_alpha_vantage = requests.get(url_alpha_vantage, params=params_alpha_vantage)
response_alpha_vantage.raise_for_status()
data_alpha_vantage = response_alpha_vantage.json()

# Filter out daily data from JSON data
daily_data = data_alpha_vantage['Time Series (Daily)']
dates = sorted(daily_data.keys(), reverse=True)

# Iterate through daily price data
# Find if there is price increase/decrease more than 5%
for i in range(1, NUM_DAYS):
    yesterday = dates[i-1]
    today = dates[i]
    yesterday_price = float(daily_data[yesterday]['4. close'])
    today_price = float(daily_data[today]['4. close'])
    percentage_change = (yesterday_price - today_price) / yesterday_price * 100

    # Get news from News API if price difference is more than 5%
    if percentage_change > 5 or percentage_change < -5:

        # Get response for News API
        params_news["from"] = yesterday
        response_news = requests.get(url_news, params=params_news)
        response_news.raise_for_status()
        data_news = response_news.json()

        # Get 3 news articles about the STOCK and send SMS
        for k in range(3):
            headline = data_news['articles'][k]['title']
            brief = data_news['articles'][k]['description']
            imoji = "🔺" if percentage_change > 5 else "🔻"

            # Create message and send SMS
            message = client.messages.create(
                body=f"\n{STOCK}: {imoji+str(round(percentage_change, 2))}%  "
                     f"\n Headline: {headline} \n Brief: {brief}",
                from_='+18623058420',
                to = '15302048374'
            )