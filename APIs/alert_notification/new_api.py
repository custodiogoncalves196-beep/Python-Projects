import requests


API_KEY = 'YOU_API_KAY'
API_URL = "https://newsapi.org/v2/everything"

parameters = {
    "q": "Tesla",
    "from": "2026-08-31",
    "sortBy": "popularity",
    "apiKey": API_KEY
}

response = requests.get(API_URL, params=parameters)
response.raise_for_status()

news_articles = response.json()
news = news_articles["articles"]


def news_article():
    mensage = ""

    for news_for in range(3):
        title = news[news_for]["title"]
        description = news[news_for]["description"]
        n_news = news_for + 1

        mensage += f"{n_news}: Title: {title}\nDescription: {description}\n"

    return mensage


