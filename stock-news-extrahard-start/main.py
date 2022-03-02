import requests

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
ALPHA_VANTAGE_API_KEY = "VZRH7X9ZESYF9PFN"
NEWS_API_KEY = "3dc2973b61764b798f5169c2a94db50e"

# Set up parameters for requests
# - For Alpha Vantage
url_alpha_vantage = 'https://www.alphavantage.co/query'
params_alpha_vantage = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": ALPHA_VANTAGE_API_KEY
}

# - For News
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
for i in range(1, 15):
    day_before_yesterday = dates[i-1]
    yesterday = dates[i]
    day_before_yesterday_price = float(daily_data[day_before_yesterday]['4. close'])
    yesterday_price = float(daily_data[yesterday]['4. close'])

    # Get news from News API if price difference is more than 5%
    if yesterday_price < day_before_yesterday_price * 0.95 or yesterday_price > day_before_yesterday_price * 1.05:

        # Get response for News API
        params_news["from"] = yesterday
        response_news = requests.get(url_news, params=params_news)
        response_news.raise_for_status()
        data_news = response_news.json()

        # Get 3 news articles about the STOCK
        for k in range(3):
            print(yesterday, data_news['articles'][k]['title'])
            print(data_news['articles'][k]['description'])


## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 


#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

