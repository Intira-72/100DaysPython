#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import FlightData


if __name__ == "__main__":
    data_m = DataManager()
    sheet_data = data_m.get_data_prices()
    
    for data in sheet_data:
        if data['iataCode'] == '':
            flight_search = FlightSearch(data['city'])
            data_m.put_iatacode(data['id'], flight_search.get_flight_search())
        
        flight_data = FlightData(data['iataCode'], data['lowestPrice'])
        [print(i) for i in flight_data.flight_data_func()]
        