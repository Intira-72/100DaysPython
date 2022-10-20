import requests
import os


SEARCH_ENDPOINT = "https://api.tequila.kiwi.com/locations/query"
HEADERS = {
    'apikey': os.environ.get("API_KEY")
    }

class FlightSearch:
    def __init__(self, city):
        self.city = city
    
    def get_flight_search(self):        
        query_params = {
            'term': self.city
        }

        resp = requests.get(url=SEARCH_ENDPOINT, headers=HEADERS, params=query_params)        
        return resp.json()['locations'][0]['code']