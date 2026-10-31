import requests
import pandas as pd
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient

API_KEY = os.environ.get("OWM_API_KEY")
OWM_URL = "https://api.openweathermap.org/data/2.5/forecast"
account_sid = "TWILIO_ACCOUNT_SID"
auth_token = os.environ.get("TWILIO_AUTH_TOKEN")


MY_LAT = 38.524590
MY_LONG = -8.893150

parameters = {
    "lat": MY_LAT,
    "lon": MY_LONG,
    "appid": API_KEY,
    "cnt": 4,
}

response = requests.get(
    OWM_URL,
    params=parameters
)
"""Serve para transformar respostas HTTP de erro numa exceção Python"""
response.raise_for_status()

weather_data = response.json()

will_rain = False
for hour_data in weather_data["list"]:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) > 700:
        will_rain = True
if will_rain:
    proxy_client = TwilioHttpClient()
    proxy_client.session.proxies = {'https': os.environ['https_proxy']}

    client = Client(account_sid, auth_token, http_client=proxy_client)
    message = client.messages \
        .create(
        body="sms_internal_alerts",
        from_="+4915888623971",
        to="+351915019502"
    )

    print(message.status)
