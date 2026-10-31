import os
import requests
from dotenv import load_dotenv


load_dotenv()
SERPAPI_ENDPOINT = "https://serpapi.com/search"

class FlightSearch:

    def __init__(self):
        self._api_key = os.environ["SERPAPI_API_KEY"]
    #This class is responsible for structuring the flight data.

    def check_flights(self, origin_city_code, destination_city_code, from_time, to_time):
        params = {
            "engine": "google_flights",
            "departure_id": origin_city_code,
            "arrival_id": destination_city_code,
            "outbound_date": from_time.strftime("%Y-%m-%d"),
            "return_date": to_time.strftime("%Y-%m-%d"),
            "type": "1",
            "adults": "1",
            "currency": "GBP",
            "api_key": self._api_key,
        }

        data_flights = None

        try:
            response = requests.get(SERPAPI_ENDPOINT, params=params)
            response.raise_for_status()
            data_flights = response.json()

        except requests.exceptions.HTTPError as errh:
            print("Http Error:", errh)
        except requests.exceptions.ConnectionError as errc:
            print("Error Connecting:", errc)
        except requests.exceptions.Timeout as errt:
            print("Timeout Error:", errt)
        except requests.exceptions.RequestException as err:
            print("OOps: Something Else:", err)
        return data_flights




