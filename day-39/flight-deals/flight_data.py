from datetime import datetime
from dateutil.relativedelta import relativedelta
import requests
import os

SEARCH_ENDPOINT = "https://api.tequila.kiwi.com/v2/search"
MY_IATA_CODE = "LON"
HEADERS = {
    'apikey': os.environ.get("API_KEY")
    }

class FlightData:
    #This class is responsible for structuring the flight data.
    def __init__(self, iata_code, lowest_price):
        self.iata_code = iata_code
        self.lowest_price = lowest_price
        self.tomorow_date = datetime.today().strftime("%d/%m/%Y")
        self.six_months_later = (datetime.today() + relativedelta(months=+6)).strftime("%d/%m/%Y")

    
    def flight_data_func(self):
        search_parama = {
            "fly_from": MY_IATA_CODE,
            "fly_to": self.iata_code,
            "date_from": self.tomorow_date,
            "date_to": self.six_months_later,
            "max_stopovers": 0,
            "curr": "GBP",
            "flight_type": "round",
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28
        }

        resp = requests.get(url=SEARCH_ENDPOINT, params=search_parama, headers=HEADERS)
        return self.price(resp.json()['data'])


    def price(self, filght_data):
        data_price = []

        min_price = min(item['price'] for item in filght_data)

        for d in filght_data:   
            if d['price'] < self.lowest_price and d['price'] <= min_price:
                data_price.append({'price': d['price'],
                                    'cityFrom': d['cityFrom'],
                                    'flyFrom': d['flyFrom'],
                                    'cityTo': d['cityTo'],
                                    'flyTo': d['flyTo'],
                                    'outbound_date': d['route'][0]['local_arrival'],
                                    'inbound_date': d['route'][1]['local_arrival']})

        return data_price

