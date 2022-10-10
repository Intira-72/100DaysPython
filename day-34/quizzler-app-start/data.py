import requests

parameters = {
    'amount': 30,
    'type': 'boolean'
}

response = requests.get(url="https://opentdb.com/api.php", params=parameters)
response.raise_for_status()
data = response.json()

question_data = data['results']


if __name__ == "__main__":
    [print(i) for i in question_data]