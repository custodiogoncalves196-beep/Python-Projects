from pprint import pprint
import requests_cache
from datetime import datetime, timedelta
from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import find_cheapest_flight

requests_cache.install_cache(
    "flight_cache",
    expire_after=3600
)

# 4. Pass the data back to the main.py file, so that you can print the data from main.py

data_manager = DataManager()
sheet_data = data_manager.get_destination_data()
# print(sheet_data)

# 5. Try importing pretty print and printing the data out again using pprint() to see it formatted.
# Print the sheet_data and verify that it includes the airport IATA codes for each city.
pprint(sheet_data)

tomorrow = datetime.now() + timedelta(days=1)
six_month_from_today = datetime.now() + timedelta(days=(6 * 30))

data_flights = FlightSearch()

data_flights_search = data_flights.check_flights(
    origin_city_code="LHR",
    destination_city_code="CDG",
    from_time=tomorrow,
    to_time=six_month_from_today
)

# pprint(data_flights_search)

# ==================== Show the Cheapest Flight ====================

cheapest_flight = find_cheapest_flight(
    data_flights_search,
    return_date=six_month_from_today.strftime("%Y-%m-%d")
)
pprint(f"{sheet_data[0]['city']}: GBP {cheapest_flight.price}")

if cheapest_flight.price != "N/A" and cheapest_flight.price < sheet_data[0]["lowestPrice"]:
    pprint(f"Lower price flight found to {sheet_data[0]['city']}!")
    data_manager.update_lowest_price(sheet_data[0]["id"], cheapest_flight.price)