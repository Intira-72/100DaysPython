import requests
import os


SHEET_ENDPOINT = "https://api.sheety.co/13e9fa9adfa318a5407978d7859c48a8/flightDeals/prices"
SHEET_HEADERS = {
    'Authorization': os.environ.get("SHEET_HEADERS")
}

class DataManager:
    def __init__(self):
        pass    

    def get_data_prices(self):
        resp = requests.get(url=SHEET_ENDPOINT, headers=SHEET_HEADERS)
        return resp.json()['prices']

    def put_iatacode(self, id, iatacode):
        flight_endpoint = f"{SHEET_ENDPOINT}/{id}"

        put_params = {
            'price': {
                'iataCode': iatacode
            }
        }

        resp = requests.put(url=flight_endpoint, headers=SHEET_HEADERS, json=put_params)
        return resp.json()['price']['iataCode']
