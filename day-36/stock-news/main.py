import requests
import os
from twilio.rest import Client

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_API_ENDPOINT = "https://newsapi.org/v2/everything"

account_sid = os.environ.get('OWN_ACC_SID')
auth_token = os.environ.get('OWN_AUTH_TOKEN')

parameters = {
    'function': 'TIME_SERIES_DAILY',
    'symbol': STOCK_NAME,
    'apikey': 'O65MGTND9130LMVF'
}

resp = requests.get(STOCK_ENDPOINT, params=parameters)
data = resp.json()

date_list_keys = [k for k in data['Time Series (Daily)'].keys()]

last_day_closing_price = float(data['Time Series (Daily)'][date_list_keys[0]]['4. close'])
before_last_day_closing_price = float(data['Time Series (Daily)'][date_list_keys[1]]['4. close'])

difference = abs(last_day_closing_price - before_last_day_closing_price)

diff_percent = (difference / last_day_closing_price) * 100

if diff_percent > 5:
    news_params = {
        'q': STOCK_NAME,
        'apiKey': '1cb6c6e2304747fc9ffa8a061f28d50f',
        'sortBy': 'popularity',
        'from': date_list_keys[0],
        'to': date_list_keys[0]
    }

    news_resp = requests.get(NEWS_API_ENDPOINT, news_params)

    articles = news_resp.json()['articles'][:3]

    list_news = [{'title': i['title'], 'description': i['description']} for i in articles]

    client = Client(account_sid, auth_token)
    
    for news in list_news:
        formated_articles = f"Headline: {news['title']}\n\nBrief: {news['description']}"
        message = client.messages.create(body=formated_articles,
                                        from_='+16403446119',
                                        to='+66984094135')
    print(message.status)

