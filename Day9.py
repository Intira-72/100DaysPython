from replit import clear
from art import logo

student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62,
}

student_grade = {}


def studentGrade():
    for i in student_scores:
        if student_scores[i] > 90:
            student_grade[i] = "Outstanding"
        elif student_scores[i] > 80:
            student_grade[i] = "Exceeds Expectations"
        elif student_scores[i] > 70:
            student_grade[i] = "Acceptable"
        else:
            student_grade[i] = "Fail"

    print(student_grade)


capitals = {
    "France": "Paris",
    "Germany": "Berlin"
}

travel_log = [
    {"country": "France",
     "cities_visited": ["Paris", "Lille", "Dijon"],
     "total_visits": 12},
    {"country": "Germany",
     "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
     "total_visits": 5}
]


def add_new_country(name, city, total):
    travel_log.append({"country": name,
                       "cities_visited": city,
                       "total_visits": total})


def secret_bidding():
    bids = {}
    bidding_finished = False

    while not bidding_finished:
        print(logo)
        name = input("What is your name?\n")
        price = int(input("What is your bid?\n$"))
        bids[name] = price
        bidding_finished = True if input("Are there any other bidding's? Type 'yes' of 'no'.") == 'yes' else False
        clear()

    win_name = ""
    top_bid = 0
    for i in bids:
        if bids[i] > top_bid:
            win_name = i
            top_bid = bids[i]

    print(f"The winner is {win_name} with a bid of ${top_bid}.")


if __name__ == '__main__':
    secret_bidding()

    # add_new_country("Russia", ["Moscow", "Saint Petersburg"], 2)
    # [print(i) for i in travel_log]

    # studentGrade()

    # print(student_scores)