import os
import requests

from datetime import datetime


MY_GENDER = "female"
MY_AGE = 30
MY_WEIGHT_KG = 55
MY_HEIGHT_CM = 151


APP_ID = os.environ.get('APP_ID')
API_KEY = os.environ.get('API_KEY')

EXERCISE_ENDPOINTS = "https://trackapi.nutritionix.com/v2/natural/exercise"


def post_exercise():
    HEADERS = {
        'x-app-id': APP_ID,
        'x-app-key': API_KEY
    }

    exercise_params = {
        "query": input("Tell me which exercise you did: "),
        "gender": MY_GENDER,
        "weight_kg": MY_WEIGHT_KG,
        "height_cm": MY_HEIGHT_CM,
        "age": MY_AGE
    }

    resp = requests.post(url=EXERCISE_ENDPOINTS, json=exercise_params, headers=HEADERS)
    return resp.json()    
        

def record_to_sheet():
    sheet_endpoint = "https://api.sheety.co/13e9fa9adfa318a5407978d7859c48a8/workoutTracking/workouts"
    workout_headers = {
        "Authorization": os.environ.get("WORKOUT_AUNT")
    }
    workout_json = post_exercise()['exercises']    

    for workout in workout_json:
        workout_params = {
            "workout": {
                "date": datetime.now().strftime("%d/%m/%Y"),
                "time": datetime.now().strftime("%H:%M:%S"),
                "exercise": workout['name'],
                "duration": workout['duration_min'],
                "calories": workout['nf_calories'],
            }
        }

        resp = requests.post(url=sheet_endpoint, json=workout_params, headers=workout_headers)
        print(resp.text)


if __name__ == "__main__":
    record_to_sheet()