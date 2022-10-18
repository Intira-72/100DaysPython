import requests
import os
from datetime import date


MY_NAME_TOKEN = os.environ.get('MY_NAME_TOKEN')
PIXELA_USERNAME = "intirav2022"

PIXELA_ENDPOINT = "https://pixe.la/v1/users"
GRAPH_ENDPOINT = f'{PIXELA_ENDPOINT}/{PIXELA_USERNAME}/graphs'

GRAPH_ID = 'graph1'

HTTPS_HEADER = {
        'X-USER-TOKEN': MY_NAME_TOKEN
    }


def registeration_pixela_users():
    user_params = {
        'token': MY_NAME_TOKEN,
        'username': PIXELA_USERNAME,
        'agreeTermsOfService': 'yes',
        'notMinor': 'yes',
        'thanksCode': '',
    }

    resp = requests.post(url=PIXELA_ENDPOINT, json=user_params)
    print(resp.text)


def create_graphs():    

    graph_params = {
        'id': GRAPH_ID,
        'name': 'Coding Graph.',
        'unit': 'Hr',
        'type': 'int',
        'color': 'ajisai'
    }   

    graph_resp = requests.post(url=GRAPH_ENDPOINT, json=graph_params, headers=HTTPS_HEADER)
    return graph_resp.text


def pixel_data():

    pixel_data_params = {
        'date': date.today().strftime("%Y%m%d"),
        'quantity': input("Enter the number of hours it takes to code. : "),
        'optionalData': ''
    }

    pixel_data_resp = requests.post(url=f"{GRAPH_ENDPOINT}/{GRAPH_ID}", json=pixel_data_params, headers=HTTPS_HEADER)
    return pixel_data_resp.text


def update_pixel_data():
    selected_date = input("Enter the date you want to edit (YYYYMMDD) : ")

    pixel_data_params = {
        'quantity': input("Enter the number of hours you want to edit : "),
    }

    pixel_data_resp = requests.put(url=f"{GRAPH_ENDPOINT}/{GRAPH_ID}/{selected_date}", json=pixel_data_params, headers=HTTPS_HEADER)
    return pixel_data_resp.text


def delete_pixel_data():
    selected_date = input("Enter the date you want to remove (YYYYMMDD) : ")

    pixel_data_resp = requests.delete(url=f"{GRAPH_ENDPOINT}/{GRAPH_ID}/{selected_date}", headers=HTTPS_HEADER)
    return pixel_data_resp.text


if __name__ == "__main__":
    print(pixel_data())