from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient
from data_acao import *
from new_api import news_article


account_sid = "   "
auth_token = os.environ.get("TOKEN")


percentage = variation(latest_close, previous_close)


if abs(percentage) >= 5:
    news = news_article()

    proxy_client = TwilioHttpClient()
    proxy_client.session.proxies = {'https': os.environ['https_proxy']}

    client = Client(account_sid, auth_token, http_client=proxy_client)
    message = client.messages \
        .create(
        body=f"TSLA teve uma variação de {percentage}%\n{news}",
        from_="  ",
        to="  "
    )

else:
    print(f"A variação foi de {percentage}%. Não é necessário procurar notícias.")
