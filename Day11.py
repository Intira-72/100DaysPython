import random
import blackjack


def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)


def calculate_score(card_list):
    score = sum(card_list)

    if score == 21 and len(card_list) == 2:
        score = 0

    if score > 21 and 11 in card_list:
        card_list[card_list.index(11)] = 1
        score = sum(card_list)

    return score


def compare(u_score, com_score):

    if com_score > 21:
        return "You're Win!"
    elif u_score > com_score:
        return "You're Win!"
    elif u_score < com_score:
        return "You're Lose!"
    else:
        return "Then it's a Draw."


def blackjack_game():
    print(blackjack.logo)

    com_cards = []
    u_cards = []
    is_game_over = False

    for _ in range(2):
        com_cards.append(deal_card())
        u_cards.append(deal_card())

    while not is_game_over:
        u_score = calculate_score(u_cards)
        com_score = calculate_score(com_cards)

        print(f'Your Cards: {u_cards}, current score: {u_score}')
        print(f"Computer's first card: [{com_cards[0]}]")

        if u_score == 0 or u_score > 21:
            is_game_over = True
            return print("Game Over! You're Lose!")
        elif com_score == 0:
            is_game_over = True
            return print(f"Game Over! You're Win!, Computer's card is {com_cards}")
        else:
            ask_new_card = input("Type 'y' to get another card, type 'n' to pass: ")

            if com_score < 17:
                com_cards.append(deal_card())

            if ask_new_card == 'y':
                u_cards.append(deal_card())
            else:
                is_game_over = True
                print(f'Your Cards: {u_cards}, current score: {u_score}')
                print(f"Computer's Card: {com_cards}, current score: {sum(com_cards)}")
                return compare(u_score, com_score)


if __name__ == '__main__':
    blackjack_game()

    # print(calculate_score([deal_card(), deal_card(), 11]))

    # print(calculate_score([1, 2, 3, 4, 5]))
